fname = document.getElementById('fname');
lname = document.getElementById('lname');
addr = document.getElementById('addr');
gender = document.getElementById('gender');
date_of_in = document.getElementById('date_of_in');
date_of_out = document.getElementById('date_of_out');
category = document.getElementById('category');
PID = document.getElementById('PID');
SID = document.getElementById('SID');
case_id = document.getElementById('case_id');
cell_id = document.getElementById('cell_id');

db = 'http://127.0.0.1:5000/'

//login functionality
function register() {
    s = new FormData();
    s.append('fname', fname.value); 
    s.append('lanme', lname.value);
    s.append('addr', addr.value);
    s.append('gender', gender.value);
    s.append('date_of_in', date_of_in.value);
    s.append('date_of_out', date_of_out.value);
    s.append('category', category.value);
    s.append('PID', PID.value);
    s.append('SID', SID.value);
    s.append('case_id', case_id.value);
    s.append('cell_id', cell_id.value);

    
    var g = $.ajax({
        url: db + 'add_prisoner', 
        type: 'POST',
        processData : false,
        contentType : false, 
        crossDomain: true,
        data: s
  
    }).done(function(data) {
        alert('Added Successfully');
        window.location = db+'prisoner.html';
  });
  }
  function test () {
    console.log(uname.value, password.value)
  }
  