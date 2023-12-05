<?php

$username = $_POST["username"];
$password = $_POST["pass"];
$doRemember_me = $_POST["remember-me"];
$isAuthenticated = False;

$encrypted_password = hash('sha512', $password);

$mariadb_server_address = 'jdbc:mariadb://localhost:3306';
$mariadb_username = 'phpstorm';
$mariadb_password = 'TROMPITA2';
$database_name = 'RTerminal';
$table_name = 'admins';


$mysqli = mysqli_connect($mariadb_server_address, $mariadb_username, $mariadb_password, $database_name);
$admins_table = mysqli_query($mysqli, "SELECT * FROM admins");

for ($i = 0; count($admins_table); $i++) {
    if ($admins_table[$i]['username'] === $username and $admins_table[$i]['password'] === $encrypted_password) {
        $isAuthenticated = True;
        break;
    }
}

setcookie("authentication", $isAuthenticated, time()+3600);
if ($doRemember_me) {
    setcookie("authentication", $isAuthenticated);
}

if ($isAuthenticated === False) {
    header("./Login_v3/status.php");
} else {
    header("./index.php");
}
