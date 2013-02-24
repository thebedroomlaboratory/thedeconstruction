<?php
$xml = simplexml_load_file("test.xml");
$con = mysql_connect("localhost","root","root");
if(!$con){
  //echo "<div id='name'> Title <br> </div>";
  //echo "<div id='temp'> Connection Open <br> </div>";
  die('Could not connect: ' . mysql_error());
}
//echo "<div id='name'>" . $xml->getName() . "<br> </div>";
//foreach($xml->children() as $child)
//{
//echo  $child->getName() . ": " . $child . "&#176;<br>";
//}
//echo "<div id='temp'>" . $xml->Temp . "&#176;<br> </div>";
//echo "<div id='temp'> Its a celebration bitches! &#176;<br> </div>";

mysql_select_db("tbl_thermostat", $con);

$result = mysql_query("SELECT * FROM tbl_room_info WHERE unique_id='1'");
while($row = mysql_fetch_array($result)){
  echo "<div id='name" . $row['unique_id'] . "'> Room " . $row['device_id'] . "<br> </div>";
  echo "<div id='temp" . $row['unique_id'] . "'> " . $row['temperature'] . "<br> </div>";
}

mysql_close($con);
?> 


