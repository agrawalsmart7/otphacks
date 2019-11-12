
<html>
<center>
	<form metho="GET" action="">
		One Time Password (OTP) <br><input type="text" name="OTP" value="" placeholder="****">
		<br><input type="submit" name="verify">
	</form>	
</center>	

</html>

<?php

$otp = @$_GET['OTP'];
$remoteaddr = $_SERVER['REMOTE_ADDR'];

if (isset($otp)){
	$command = "python verifyotp.py $remoteaddr";
	$data = exec($command);
	
	$command2 = "python rate_limiting.py $remoteaddr";
	$data2 = exec($command2);
	if ($data2){
		echo "$data2";
	}
	else{
	echo ("You have provided this $otp<br>");
	
	
	if ($data == $otp){
		
		
		echo  ("Success! You Submitted valid OTP");
		

		}
	else{
		echo ("Please give valid OTP");
		}
	}
}


?>
