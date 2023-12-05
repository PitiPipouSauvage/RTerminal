<?php
//if (!isset($_COOKIE) or $_COOKIE["authentication"] === False) {
//    header('../../../../login.php');
//    exit;
//} else {
//    $isLogged_in = True;
//}

$mariadb_server_address = 'jdbc:mariadb://localhost:3306';
$mariadb_username = 'phpstorm';
$mariadb_password = 'TROMPITA2';
$database_name = 'RTerminal';
$table_name = 'bots';

$connection = mysqli_connect($mariadb_server_address, $mariadb_username, $mariadb_password, $database_name);
?>

<!doctype html>
<html lang="en">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="fonts/icomoon/style.css">
<link rel="stylesheet" href="css/owl.carousel.min.css">

<link rel="stylesheet" href="css/bootstrap.min.css">

<link rel="stylesheet" href="css/style.css">
<title>Table #6</title>
</head>
<body>
<div class="content">
<div class="container">
<h2 class="mb-5">Bots list</h2>
<div class="table-responsive">
<table class="table table-striped custom-table">
<thead>
<tr>
<th scope="col">IP Addresses V4</th>
<th scope="col">Role</th>
<th scope="col">Group id</th>
<th scope="col">State</th>
<th scope="col">Hash rate</th>
<th scope="col"></th>
</tr>
</thead>
<tbody>
<!-- START -->
<?php $query = "SELECT * FROM bots";
$output = mysqli_query($connection, $query);
?>
<?php foreach($output as $id=>$bot):?>
    <tr scope="row">
        <td><?php echo($bot['ip_addressV4']);?></td> <!-- Ip address -->
        <td><a href="#"><?php echo($bot['role']);?></a></td> <!-- Role -->
        <td><?php echo($bot['group_id']);?>></td> <!-- Group id -->
        <td><?php echo($bot['state']);?></td> <!-- State -->
        <td><?php echo($bot['hash_rate']);?></td> <!-- Hash rate -->
    </tr>
<?php endforeach;?>
<!-- END -->
<tr>
<td>4616</td>
<td><a href="#">Matthew Wasil</a></td>
<td>
Graphic Designer
<small class="d-block">Far far away, behind the word mountains</small>
</td>
<td>+02 020 3994 929</td>
<td>London College</td>
<td><a href="#" class="more">Details</a></td>
</tr>
<tr>
<td>9841</td>
<td><a href="#">Sampson Murphy</a></td>
<td>
Mobile Dev
<small class="d-block">Far far away, behind the word mountains</small>
</td>
<td>+01 352 1125 0192</td>
<td>Senior High</td>
<td><a href="#" class="more">Details</a></td>
</tr>
<tr>
<td>9548</td>
<td><a href="#">Gaspar Semenov</a></td>
<td>
Illustrator
<small class="d-block">Far far away, behind the word mountains</small>
</td>
<td>+92 020 3994 929</td>
<td>College</td>
<td><a href="#" class="more">Details</a></td>
</tr>
<tr>
<td>4616</td>
<td><a href="#">Matthew Wasil</a></td>
<td>
Graphic Designer
<small class="d-block">Far far away, behind the word mountains</small>
</td>
<td>+02 020 3994 929</td>
<td>London College</td>
<td><a href="#" class="more">Details</a></td>
</tr>
<tr>
<td>9841</td>
<td><a href="#">Sampson Murphy</a></td>
<td>
Mobile Dev
<small class="d-block">Far far away, behind the word mountains</small>
</td>
<td>+01 352 1125 0192</td>
<td>Senior High</td>
<td><a href="#" class="more">Details</a></td>
</tr>
<tr>
<td>9548</td>
<td><a href="#">Gaspar Semenov</a></td>
<td>
Illustrator
<small class="d-block">Far far away, behind the word mountains</small>
</td>
<td>+92 020 3994 929</td>
<td>College</td>
<td><a href="#" class="more">Details</a></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
<script src="js/jquery-3.3.1.min.js"></script>
<script src="js/popper.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/main.js"></script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v84a3a4012de94ce1a686ba8c167c359c1696973893317" integrity="sha512-euoFGowhlaLqXsPWQ48qSkBSCFs3DPRyiwVu3FjR96cMPx+Fr+gpWRhIafcHwqwCqWS42RZhIudOvEI+Ckf6MA==" data-cf-beacon='{"rayId":"82dd8eae7de803f1","b":1,"version":"2023.10.0","token":"cd0b4b3a733644fc843ef0b185f98241"}' crossorigin="anonymous"></script>
</body>
</html>