// jQuery & Velocity.js
// alert('here');
$(document).on('keypress', function (e) {
  if(e.which == 13){
    // alert('here');
    $('#login-button').click();
  }
});

var myInput = document.getElementById("password_input");
var validpass1 = /[a-z]/g;
var validpass2 = /[A-Z]/g;
var validpass = /[0-9]/g;


function slideUpIn() {
  $("#login").velocity("transition.slideUpIn", 1250)
}

function slideLeftIn() {
  $(".row").delay(500).velocity("transition.slideLeftIn", {stagger: 500})
}

function shake() {
  $(".password-row").velocity("callout.shake");
}

slideUpIn();
slideLeftIn();

// please look at the if statement if its true it should lead to the given webpage, for the time being i havent done anything
$("#login-button").on("click", function () {
  if(myInput.value.match(validpass) && myInput.value.match(validpass1) && myInput.value.match(validpass2) && (myInput.value.length >= 8))
  {
   submit_data();
  }
  else{
    //shake();
    submit_data(); // remove Only for testing
  }
});

function submit_data() {
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  alert(csrftoken);
  // alert($('#password_input').val() + '--' + $('#username_input').val());
   $.ajax({
                url: '/login_auth/',
                type: 'POST',
                crossOrigin: true,
                crossDomain: true,
                data:{
                    'csrfmiddlewaretoken':csrftoken,
                    'password':  $('#password_input').val(),
                    'username': $('#username_input').val()

                },
                error: function () {
                    alert('Could not connect to server...');
                },
                success: function(response_ds) {
                    // alert(response_ds);
                    window.location.href = '/';
                }
        	});
}
