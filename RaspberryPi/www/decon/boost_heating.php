<?php
function boost(){
  $con = mysql_connect("localhost","root","root");
  // if the connection  doesn't exist throw error
  if(!$con){
    die('Could not connect: ' . mysql_error());
  }
  // select db
  mysql_select_db("tbl_thermostat", $con);

  // perform insert 
  mysql_query("INSERT INTO tbl_heating VALUES (true, 2)")

  // close connection
  mysql_close($con);
}

// call function to insert data
boost();

?>
