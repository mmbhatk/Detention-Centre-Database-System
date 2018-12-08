wardens = document.getElementById('wardens');
db = 'http://127.0.0.1:5000/'

var g = $.ajax({
    url: db + 'browse_officer/1111111111', 
    type: 'GET',
    processData : false,
    contentType : false, 
    crossDomain: true,

}).done(function(data) {
    warden = data;
    wardens.innerHTML = data;
});