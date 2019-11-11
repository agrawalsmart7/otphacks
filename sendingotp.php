<?php 
 
$email = $_GET['Email'];
if (isset($email)){
	
	$command = "python3 sendotp.py $email";
	exec($command);
	

	header("Location: verifyotp.php");
	
};

?>