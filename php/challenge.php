<!DOCTYPE HTML>
<!-- This is the Goose Home Page 
	The purpose of this page is to display the list 
	of the top sql-injectors! It makes a call to the 
	local database, to search for specifc people, or for 
	everyone if the text is blank

	SQL Statement are hard to provision in MYSQL, so I just
	Decided to put the statement directly in the request from
	this page. As long as people just search for names in the 
	searchbox, it should be completely fine! I have limited the
	Database users privileges to just SELECT and INSERT, so the risk
        is low! I mean, it's not like many people know how to end a SQL 
	command anyway... (as long as they don't look at
	www.w3schools.com/sql/sql_injection.asp, especially the part about
	SQL Injection Based on Batched SQL Statements )
-->

<HTML>
	<HEAD>
		<Title>Challenge Top Performers Table</TITLE>
	</HEAD>
	<BODY>
		<H1>Welcome to the top performers page!</H1>
		<!-- I always forget the database schema, so this note is to
	  	     remind me - the table is called "topperformers" and it has
		     two columns - VARCHAR (20) name & VARCHAR (20) team -
		     Remeber to remove this comment before you publish the 
		     webpage...
		-->
		<P>This page contains a list of all the top performers of the challenges</p>
		<P>You can search the database using the search form, or leave it blank to see everyone</p>

		<?php
		ini_set('display_errors', 'Off');

		$servername = "localhost";
		$username = "maryonthedb";
		$password = "2345snjkdf89wsa";
		$dbname = "TOPPERFORMERS";


		$conn = new mysqli($servername, $username, $password, $dbname);

		//Check the connection
		if (mysqli_connect_error()) {
			die("Connection failed: " . mysqli_connect_error());
		}

		//Get the Form Data that was submitted

		$form_name = $_POST['name'];

			
		//If it is blank return everything
		if(empty($form_name)) {
			$sql = "SELECT * FROM topperformers";
		}
		else {

		        //otherwise return the query
			$sql = "SELECT * FROM topperformers WHERE name LIKE '" . $form_name ."'";
		}
		
		
		echo "<!-- SQL STATEMENT: " . $sql . "   -->";



		if (mysqli_multi_query($conn, $sql)) {
		    do {
		            /* store first result set */
		        if ($result = mysqli_store_result($conn)) {
		                while ($row = mysqli_fetch_row($result)) {
					echo "<b>Name:</b> " . $row[0] . "      -     <b>Team:</b> " . $row[1] . "<br>";

			        	}
		            	mysqli_free_result($result);
		        	}
            			
        		} while (mysqli_next_result($conn));
		}



		mysqli_close($conn);
		 
?>

<br><br><br>

<form action="challenge.php" method="post">
Name: <input type="text" name="name">
&nbsp;&nbsp;&nbsp;&nbsp;
<input type="submit">
</form>

