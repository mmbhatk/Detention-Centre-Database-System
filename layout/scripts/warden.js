name = document.getElementById('name');
WID = document.getElementById('WID');
OID = document.getElementById('OID');
salary = document.getElementById('salary');


//login functionality
function register() {
    s = new FormData();
    s.append('name', name.value);
    s.append('WID', WID.value);
    s.append('OID', OID.value);
    s.append('salary', salary.value);
    
    var g = $.ajax({
        url: db + 'login', 
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
  