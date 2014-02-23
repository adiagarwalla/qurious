// this is the inclass.js file for javascript related to the inclass stuff.
      function sessionConnectedHandler (event) {
	     subscribeToStreams(event.streams);
	     session.publish(publisher);
	  }

	  function streamCreatedHandler(event) {
	    subscribeToStreams(event.streams);
	  }

	  function subscribeToStreams(streams) {
	    for (var i = 0; i < streams.length; i++) {
	        var stream = streams[i];
	        if (stream.connection.connectionId 
	               != session.connection.connectionId) {
	            session.subscribe(stream, "mySubscriberElement", {width: 1200, height: 600});
                var myCountdown2 = new Countdown({time: 60 * time, width:200, height:80, rangeHi:"hour", target:"countdown_timer"});
	        }
	    }
	  }
 
    function streamDestroyedHandler(event) {
        for (var i = 0; i < event.streams.length; i++) {
            var stream = event.streams[i];
            if (stream.connection.connectionId 
                 != session.connection.connectionId) {             
                $('#myModalInstructor').modal({ backdrop: 'static', keyboard: false, show: true });
            }
        }
    }

    function exitSessionNotification() {

      session.unpublish(publisher);
      $('#myModal').modal('hide')
      $('#myModalReview').modal('show')

    }
	  //}

	  // else
	  // {
	  // 	TB.log("The client does not support WebRTC.");
	  // }
	  	 
	  // Figure out if required. If yes, then what exactly to do when for some reason connection fails
	  // TB.addEventListener("execption", exceptionHandler);

	  // Detecting if a user has disconnected
	  function disconnect() {
	  		session.addEventListener("sessionDisconnected", sessionDisconnectedHandler);
	  		session.connect(apiKey, token);
	  }

	  function sessionDisconnectedHandler(event){
	  	if (event.reason == "networkDisconnected") {
	  		alert("Your network connection terminated.")
	  	}
	  }

	  // function connectionCreatedHandler(event) {
   //  	connectionCount += event.connections.length;
   //  	TB.log(connectionCount);
	  // }
 
	  // function connectionDestroyedHandler(event) {
   //  	connectionCount -= event.connections.length;
   //  	TB.log(connectionCount);
	  // }	


    // Toggle stuff for chat window
    function toggle_visibility(id, id2) {
       var e = document.getElementById(id);
       var e2 = document.getElementById(id2);
       if(e.style.display == 'block')
       {
          e.style.display = 'none';
          e2.style.marginRight = "30px";
       }
       else
       {
          e.style.display = 'block';
          e2.style.marginRight = "294px";
       }
    }

    // function publisher_change(id) {
    //    var e = document.getElementById(id);
    //    if(e.style.marginRight == 'block')
    //       e.style.display = 'none';
    //    else
    //       e.style.display = 'block';
    // }

function get_chat_message() {
    // this function gets the chat messages
    // for this session
    $.get('/inclass/chat/' + sessionId + '/' + message_num + '/', function( data ) {
        // update the proper div with the new chat messages., update message num to be the message num of the last message
        // you get an array back of message objects
        // time to populate them with the for loop through :D
        for(i = 0; i < data.length; i++) {
            $("#chatWindowContent").append("<b>" + data[i].fields.user_from_name + ":</b> " + data[i].fields.content + "<br>");
            message_num = Math.max(message_num, data[i].fields.seq_number);
        }
    }).done(function() {
        get_chat_message();
    });
}

