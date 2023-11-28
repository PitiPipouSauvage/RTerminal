<?php

$username = $_POST["username"];
$password = $_POST["pass"];

$mariadb_server_address = 'localhost';
$mariadb_username = 'phpstorm';
$mariadb_password = 'TROMPITA2';
$database_name = 'RTerminal';
$table_name = 'admins';

$mysqli = mysqli_connect($mariadb_server_address, $mariadb_username, $mariadb_password, $database_name);

$admins_table = mysqli_query($mysqli, "SELECT * FROM admins");
