<html>
<body>

Kick time was recorded <?php echo $_POST["kicktime"]; ?>

<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = $_POST["kicktime"];
fwrite($myfile, $txt);
fclose($myfile);
echo "done";
?>

</body>
</html>
