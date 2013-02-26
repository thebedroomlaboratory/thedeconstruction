<html>
<head>
	<script src="http://code.jquery.com/jquery-latest.js"></script>
<script>
 $(document).ready(function() {
 	 $("#responsecontainer").load("response_r1.php");
   var refreshId = setInterval(function() {
      $("#responsecontainer").load('response_r1.php?randval='+ Math.random());
   }, 10000);
   $.ajaxSetup({ cache: false });
});
</script>

<title>The Bedroom Laboratory - Decon</title>
        
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"> 

		<!-- Stylesheets -->
		<link rel="stylesheet" href="css/main.css">
		<link rel="stylesheet" href="css/skeleton.css">
      
	
	</head>

	<body>

			<div style="display: block;" class="container">	
<!-- Logo -->
				<div class="sixteen columns logo">
						<a href="#">
						<img src="logo.jpg" alt="logo" height="100" width="380">
						</a>
				</div>

<!-- Navigation Bar -->

				<div class="sixteen columns">

					<div id="nav">

						<ul>
							<li class="first"><a href="index.html">About</a></li>
							<li class=""><a href="room1.php">Room 01</a></li>
							<li class="last"><a href="room2.php">Room 02</a></li>
						</ul>

					</div>

				</div>
<!-- H1 -Main Title -->

				<div class="sixteen columns content">
                <h1>Room 01</h1><br> <br>
                <div id="responsecontainer">
</div>
                
					<div class="section clearfix">
                    

        
<!-- Footer -->
				<div class="sixteen columns content">

					<div class="clearfix section" id="footer">

	<hr>
						<p class="foot">
                        
                       <p></p>
                         

					</div>

				</div>

			</div>	
	
		
</body></html>
