<?php
// import credentials
include('mysql_credentials.php');

// Open SQL Server connection
$con = new mysqli( $mysql_server, $mysql_user, $mysql_pass, $mysql_db );

// Check for SQL error
if ($con->connect_error) die ("Connection failed: " .$con->connect_error);

$search = $_GET['search'];

//select * from items where name like '%' OR true -- - %'
//SELECT * FROM items WHERE name LIKE '%' UNION SELECT username,password FROM users -- - %'
$query = "SELECT * FROM items WHERE name LIKE '%$search%'";
$result = $con->query($query);
echo $con->error;

while( $row = $result->fetch_assoc() ) {
  $name = $row["name"];
  $price = $row["price"];
  echo " - $name   $price.00 € <br/>";
}

$con->close();
