<!DOCTYPE html>
<html>
<body>
<p>Hello</p>
<button type="button" onclick="
	<?php $output = array();
	exec("checkPin4.py", $output);
	var_dump( $output);
	 ?>
">Click Me!</button>
 
</body>
</html>
