<?php
$connection = mysqli_connect('jdbc:mariadb://localhost:3306', 'phpstorm', 'TROMPITA2', 'RTerminal');
$result = mysqli_query($connection, "SELECT * FROM bots");
echo($result);