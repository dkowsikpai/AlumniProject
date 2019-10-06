// jQuery & Velocity.js

var myInput = document.getElementById("password_input");
var validpass1 = /[a-z]/g;
var validpass2 = /[A-Z]/g;
var validpass = /[0-9]/g;


function slideUpIn() {
  $("#login").velocity("transition.slideUpIn", 1250)
};

function slideLeftIn() {
  $(".row").delay(500).velocity("transition.slideLeftIn", {stagger: 500})
}

function shake() {
  $(".password-row").velocity("callout.shake");
}

slideUpIn();
slideLeftIn();

// please look at the if statement if its true it should lead to the given webpage, for the time being i havent done anything
$("button").on("click", function () {
  if(myInput.value.match(validpass) && myInput.value.match(validpass1) && myInput.value.match(validpass2) && (myInput.value.length >= 8))
  {
    // alert("hi");
    submit_auth();
  }
  else{
    shake();
  }
});