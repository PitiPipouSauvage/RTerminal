<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Botnet Status</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="status.css" />
    </head>
    <body>
<?php

$icon = <<<ICON
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
ICON;

class Machine {
    private $types = ["bot", "commander", "main_server", "mysql_server"];
    private $ip;
    private $group_id;
    private $isMining;
    private $hash_rate;
    private $type;
    private $intels = array();

    public function __construct($ip, $group_id, $isMining, $type, $hash_rate=null) {
        $this->intels["ip"] = $ip;
        $this->intels["group_id"] = $group_id;
        $this->intels["isMining"] = $isMining;
        $this->intels["hash_rate"] = $hash_rate;
        $this->intels["type"] = $type;
    }

    public function display() {
        return <<<HTML
        <span>
            <ul class="intels">
                <li>{$this->intels["ip"]}</li>
                <li>{$this->intels["group_id"]}</li>
                <li>{$this->intels["type"]}</li>
                <li>{$this->intels["isMining"]}</li>
                <li>{$this->intels["hash_rate"]}</li>
            </ul>
        </span>
        HTML;
    }
}

function main() {
    $machine = new Machine('127.0.0.1', 1, True, "bot", 34000);
}

main();
?>
    <p><?php echo($machine->display()) ?></p>
</body>
</html>