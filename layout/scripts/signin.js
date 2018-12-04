db = "http://127.0.0.1:5000/"
uname = document.getElementById('uname');
password = document.getElementById('password');
var OID;

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


function render_options() {
  document.body.innerHTML=`
  <div class="split left">
    <div class="centered">
      <button class="button" id="database"><a href="db.html"><img src="./images/demo/database.jpg" alt="Avatar woman"></button>
      <h2>Browse Database</h2></a>
    </div>
  </div>
  <div class="split center">
      <div class="centered">
        <button class="button" id="prisoner"><a href="prisoner.html"><img src="./images/demo/handcuff.png" alt="Handcuff"></button>
        <h2>Add Prisoner</h2></a>
      </div>
    </div>
  <div class="split right">
    <div class="centered">
      <button class="button" id="warden"><a href="warden.html"><img src="./images/demo/warden.png" alt="Avatar man"></button>
      <h2 style="color: black;">Add Warden</h2></a>
    </div>
  </div>
       `
}


//login functionality
function login() {
  s = new FormData();
  s.append('username', uname.value);
  s.append('password', password.value);
  var g = $.ajax({
      url: db + 'login', 
      type: 'POST',
      processData : false,
      contentType : false, 
      crossDomain: true,
      data: s

  }).done(function(data) {
      if (data.login == 'true') {
        OID = data.OID;
        render_options();
      }
      else alert('login credentials invalid');
});
}

function test () {
  console.log(uname.value, password.value)
}
