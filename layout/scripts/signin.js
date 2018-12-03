db = "http://127.0.0.1:5000/"
uname = document.getElementById('uname');
password = document.getElementById('password');

var vContinue = document.getElementById("continue"),
    vLogin = document.getElementById("login");

vContinue.addEventListener("click", function() {
   document.body.className += ' denied';
}, false);

var pfx = ["webkit", "moz", "MS", "o", ""];
function PrefixedEvent(element, type, callback) {
  for (var p = 0; p < pfx.length; p++) {
    if (!pfx[p]) type = type.toLowerCase();
    element.addEventListener(pfx[p]+type, callback, false);
  }
}

PrefixedEvent(vLogin, "AnimationEnd", function () {
  document.body.className = '';
});


//login functionality
function login() {
  s = new FormData();
  s.append('username', uname.value);
  s.append('password', password.value)
  var g = $.ajax({
      url: db + 'login', 
      type: 'POST',
      processData : false,
      contentType : false, 
      crossDomain: true,
      data: s

  }).done(function(data) {
      if (data.login == 'true') window.location = db+'officer.html';
      else alert('login credentials invalid');
});
}
function test () {
  console.log(uname.value, password.value)
}
