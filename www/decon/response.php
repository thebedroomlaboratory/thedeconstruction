<?php
$xml = simplexml_load_file("test.xml");

echo "<div id='name'>" . $xml->getName() . "<br> </div>";

//foreach($xml->children() as $child)
  //{
  //echo  $child->getName() . ": " . $child . "&#176;<br>";
  //}
  
  echo "<div id='temp'>" . $xml->Temp . "&#176;<br> </div>";
?> 


