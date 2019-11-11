
<html>
<center>
	<form metho="GET" action="">
		One Time Password (OTP) <br><input type="text" name="OTP" value="" placeholder="****">
		<br><input type="submit" name="verify">
	</form>	
</center>	

</html>

<?php

$otp = $_GET['OTP'];

if (isset($otp)){
	echo ("You have provided this $otp<br>");
	$command = "python verifyotp.py";
	$data = exec($command);
	if ($data == $otp){
		echo  ("Success! You Submitted valid OTP");

	}
	else{
		echo ("Please give valid OTP");
	}
}


?>
