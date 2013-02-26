<?php

$con = mysql_connect("localhost","root","root");
// if the connection doesn't exist throw error
if(!$con){
  die('Could not connect: ' . mysql_error());
}

mysql_select_db("tbl_thermostat", $con);

// Perform Query
$result = mysql_query("SELECT * FROM tbl_room_info WHERE device_id='1' ORDER BY unique_id DESC LIMIT 1");

// Check result
// This shows the actual query sent to MySQL, and the error. Useful for debugging.
if(!$result){
  $message  = 'Invalid query: ' . mysql_error() . "\n";
  $message .= 'Whole query: ' . $query;
  die($message);
}

// Use result
while($row = mysql_fetch_array($result)){
  // Temperature
  $temperature = $row['temperature'];
  if($temperature != NULL){
    $fileName = determineImageFileName($temperature);
    echo "<div id='temp" . $row['device_id'] . "'> " 
    . " Temperature: " .  $row['temperature'] . " &#176;<br>"
    . "<img src='img/" . $fileName . "'> "
    //. " <img src='img/tbl_snowflake.jpg'>"
    . " <br></div>";
  }

  // Humidity
  if($row['humidity'] != NULL){
    echo "<div id='humidity" . $row['device_id'] . "'> "
    . " Humidity: " . $row['humidity'] . " &#37;<br></div>";
  }

  // Light
  $light = $row['light'];
  if($light != NULL){
    $lightDesc = determineBrightness($light);
    if($lightDesc != NULL){
      echo "<div id='light" . $row['device_id'] . "'> "
      .  $lightDesc . "<br></div>"; 
    }
  }
  
  // Occupancy
  $occupancy = $row['occupancy'];
  if($occupancy != NULL){
    if($occupancy){
      echo "<div id='occupancy" . $row['device_id'] . "'> "
      . "Room has occupants <br></div>";
    }else{
      echo "<div id='occupancy" . $row['device_id'] . "'> "
      . " Room empty <br></div>";
    } 
  }
}
// Close connection
mysql_close($con);

// switch function for light
// 0. Very Dark, 1. Dark, 2. Normal, 3. Bright, 4.Very Bright
function determineBrightness($light){
  switch($light){
    case 0:
      return "Very Dark";
    case 1:
      return "Dark";
    case 2:
      return "Normal";
    case 3:
      return "Bright";
    case 4:
      return "Very Bright";
    default:
      return NULL;
  }
}

// determines the file name of  temperature image based on the temperature value
function determineImageFileName($temp){
  if($temp < 18){
   return "tbl_snowflake.jpg";
  }else if($temp > 22){
   return "tbl_sun.jpg";
  }else{
   return "tbl_leaf.jpg";
  }
}

?> 


