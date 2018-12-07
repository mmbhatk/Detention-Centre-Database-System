fname = document.getElementById('fname');
lname = document.getElementById('lname');
OID = document.getElementById('OID');
title = document.getElementById('title');
status = document.getElementById('status');
phone = document.getElementById('phone');
salary = document.getElementById('salary');
uname = document.getElementById('uname');
password = document.getElementById('password');

//login functionality
function register() {
    s = new FormData();
    s.append('fname', fname.value);
    s.append('lname', lname.value);
    s.append('OID', OID.value);
    s.append('title', title.value);
    s.append('status', status.value);
    s.append('phone', phone.value);
    s.append('salary', salary.value);
    s.append('uname', uname.value);
    s.append('password', password.value);
    
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
  