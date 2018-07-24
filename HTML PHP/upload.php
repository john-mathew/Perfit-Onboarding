<!DOCTYPE html>

<?php

 $uname = trim($_REQUEST['username']);
 $pword = trim($_REQUEST['password']);
 $fname = $_REQUEST["fname"];
 $lname = $_REQUEST["lname"]; 
 $dob = $_REQUEST["dob"];
 $bg = $_REQUEST["bg"];
 $cno = $_REQUEST["cno"];


$conn = mysqli_connect("localhost", "id6552257_perfit_training", "password", "id6552257_perfit_training");  // Check connection
  if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
  } 

  $sqlUp =  "UPDATE PerfitLogin SET FirstName ='".$fname."',LastName ='".$lname."',DoB ='".$dob."', BloodGroup = '".$bg."',ContactNo ='".$cno."' WHERE username = '".$uname."'";
    $resultUp = $conn->query($sqlUp);

 include 'Details.php';
 ?>
<html>
    <input type="hidden" name="username" value = "<?php echo $uname;?>"/>
	<input type="hidden" name="password" value = "<?php echo $pword;?>"/>
</html>
