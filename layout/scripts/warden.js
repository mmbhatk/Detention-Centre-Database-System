Name = document.getElementById('Name');
WID = document.getElementById('WID');
OID = document.getElementById('OID');
salary = document.getElementById('salary');

db = 'http://127.0.0.1:5000/'

//login functionality
function register() {
    s = new FormData();
    s.append('name', Name.value);
    s.append('WID', WID.value);
    s.append('OID', OID.value);
    s.append('salary', salary.value);
    
    var g = $.ajax({
        url: db + 'add_warden', 
        type: 'POST',
        processData : false,
        contentType : false, 
        crossDomain: true,
        data: s
  
    }).done(function(data) {
        window.location = db+'login.html';
  });
  }
  function test () {
    console.log(uname.value, password.value)
  }
  