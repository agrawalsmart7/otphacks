<?php 
 
$email = $_GET['Email'];
if (isset($email)){
	
	$command = "sendotp.py $email";
	exec($command);
	

	header("Location: verifyotp.php");
	
};

?>