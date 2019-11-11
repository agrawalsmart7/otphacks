<?php
session_start();
?>

<html>
<title>OTP Demo App</title>
<center>
	<h1> OTP Demo Application </h1>
	<form method="GET" action="sendingotp.php">
		EMail <input type="text" name="Email" id="email" value="<?php echo htmlentities(@$_GET['email'])?>">
		<input type="submit" name="submit" value="Send">
	</form>
</center>	
</html>

