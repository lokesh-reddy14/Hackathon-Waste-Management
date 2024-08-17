<?php
$servername = "localhost";
$username = "id22164679_admin123";
$password = "Admin@123";
$dbname = "id22164679_users";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$name = $_POST['name'];
$category = $_POST['category'];
$purchaseDate = $_POST['purchaseDate'];
$replacementDate = $_POST['replacementDate'];

$sql = "INSERT INTO items (name, category, purchase_date, replacement_date) VALUES ('$name', '$category', '$purchaseDate', '$replacementDate')";

if ($conn->query($sql) === TRUE) {
    header("Location: analytics.html");
    exit();
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
