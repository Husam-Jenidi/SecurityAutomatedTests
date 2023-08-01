<?php
// import credentials
include('mysql_credentials.php');
// Open SQL Server connection
$conn = new mysqli( $mysql_server, $mysql_user, $mysql_pass, $mysql_db );
// Check for SQL error
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  
  

#$user = $_GET['user'];
#$pass = $_GET['pass'];

$user = $_POST['user'];
$pass = $_POST['pass'];


// $query = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
// FIXED - no more attacks on $user
$query = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
// NOPE - $pass -> any' OR 'a'='a
// SELECT * FROM users WHERE username='admin' AND password='any' OR 'a'='a'
$result = $conn->query($query);

if($result->num_rows == 1) {
// Not specific
// if($result->num_rows == 1) {
//  [spoilers] This is still bypassable
  $row = $result->fetch_assoc();
  $username = $row["username"];
  echo "Welcome $username!";
} else {
  echo "Wrong username or password";
  // can't we just say if the username or the password were wrong?
  // Generic errors >>>>> Specific errors
}

$conn->close();
?> 