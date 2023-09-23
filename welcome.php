<html>
<body>

Welcome <?php echo $_POST["name"]; ?><br>
Your email address is: <?php echo $_POST["email"]; ?>

<?php
/*
echo readfile("newfile.txt");
*/
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = $_POST["name"];
fwrite($myfile, $txt);
$txt = $_POST["email"];
fwrite($myfile, $txt);
$txt = time();
fwrite($myfile, $txt);
fclose($myfile);
echo "done";
?>

</body>
</html>
