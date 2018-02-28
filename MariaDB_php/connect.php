<html>

<head>

<style>

body {
    background-color: #f9c68c;
}


h1 {
    color: white;
    text-align: center;
    font-family: impact;
}


p {
    font-family: verdana;
    font-size: 20px;
    font-weight: bold;
}

</style>

</head>


<body>


<h1>Returning results for lookup:</h1>


<?php echo "Search term: " . $_GET["serial"] . "<br>";


$servername = "WhoIsMysterion";

$username = "AddUserHere";

$password = "";

$dbname = "DBStoreNameHere";



// Create connection

$conn = new mysqli($servername, $username, $password, $dbname);


// Check connection

if ($conn->connect_error) 
{
    
	die("Connection failed: " . $conn->connect_error);

}



$sql = "SELECT id, serial, model FROM items WHERE serial=\"" . $_GET["serial"] . "\"";

$result = $conn->query($sql);


if ($result->num_rows > 0) 
{
    
	// output data of each row
    while($row = $result->fetch_assoc()) 
	{
        
		echo "<br> ID: ". $row["id"]. " - Serial: ". $row["serial"]. " - Item: " . $row["model"] . "<br>";
    
	}

} 
else 
{
    
	echo "0 results";

}



$conn->close();

?>

</body>

</html>
