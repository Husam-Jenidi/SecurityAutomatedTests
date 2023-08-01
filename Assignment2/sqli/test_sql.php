<?php
// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Import credentials
require_once('mysql_credentials.php');

// Open MySQL server connection
$conn = new mysqli($mysql_server, $mysql_user, $mysql_pass, $mysql_db);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

// Close the connection
$conn->close();
?>
