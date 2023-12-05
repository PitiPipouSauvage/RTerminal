<?php
$icon = <<<ICON
█▀█ █▀█ ▀▀▀█ 
░▄▀ ░▄▀ ░░█░ 
█▄▄ █▄▄ ░▐▌░
ICON;

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

echo('i love poop');

$connection = new PDO("mysql:host=localhost;dbname=RTerminal", "phpstorm", "TROMPITA2");
$connection->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, false);

$result = $connection->query("SELECT * FROM bots");
foreach($result as $row) {
    echo($row) .PHP_EOL;
}

echo('i love poop again');



echo('i love poop all the time');