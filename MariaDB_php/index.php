<!DOCTYPE html>

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
}
.container {
    width: 500px;
    clear: both;
}

.container input {
    width: 100%;
    clear: both;
}   

</style>

</head>


<body>


<h1> I'm Super Serial Guys! </h1>


<div class="container">

<form action="connect.php" method="get">
Serial: <input type="text" name="serial"><br>
<input type="submit">
</form>

<br><br>

<form action="updatedb.php" method="get">
ID:        <input type="text" name="serial"><br>
Serial:    <input type="text" name="serial"><br>
Model:     <input type="text" name="serial"><br>
IMEI:      <input type="text" name="serial"><br>
MacAddr:   <input type="text" name="serial"><br>
Notes:     <input type="text" name="serial"><br>
           <input type="submit">
</form>

</div>


</body>


</html>
