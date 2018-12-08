wardens = document.getElementById('wardens');
pdiv = document.getElementById('prisoners');

db = 'http://127.0.0.1:5000/'
var warden;
keys = ['Name', 'Warden ID', 'Salary', 'Officer ID']

function clearall() {
    w = document.getElementsByClassName("warden");
    for (var i = 0; i < w.length; i++) {
    w[i].classList.remove('selected');
        
      }
}

function setSelected(elem){
    console.log(elem);
    elem.classList.add('selected');
}


var g = $.ajax({
    url: db + 'browse_officer/'+localStorage.OID, 
    type: 'GET',
    processData : false,
    contentType : false, 
    crossDomain: true,

}).done(function(data) {
    console.log(data);
    warden = data;
    wlist = ``;
    warden.forEach(function (entry) {
        entry[2] = '$'+entry[2];
        wlist+=`<br><div onclick="prisoners(${entry[1]},this);" class="warden">`;
        for (var i = 0; i < entry.length; i++) {
            wlist+=`<span>${keys[i]}: ${entry[i]}</span><br>`;
          }
        wlist+=`</div><br>`;
        
        
      });
    wardens.innerHTML = wlist;
});

function prisoners(WID, elem) {
    clearall();
    setSelected(elem);
    console.log(WID);
    var p = $.ajax({
        url: db + 'browse_warden/'+WID, 
        type: 'GET',
        processData : false,
        contentType : false, 
        crossDomain: true,
    
    }).done(function(data) {
        console.log(data);
        prisoner = data;
        plist = ``;
        prisoner.forEach(function (e) {
            plist+=`<br><div class="prisoner">
            <span>PID: ${e[0]}</span><br>
            <span>Name: ${e[1]} ${e[2]}</span><br>
            <span>Address: ${e[3]} </span><br>
            <span>Category: ${e[4]} </span><br>
            <span>Period of imprisonment: ${e[5]} to ${e[6]}</span><br>
            <span>Gender: ${e[7]}</span><br>
            <span>Salary: $${e[8]}</span><br>
            <span>Cell ID: ${e[9]}</span><br>
            <span>Section: ${e[10]}</span><br>
            <span>Case ID: ${e[11]}</span>
        </div>
        <br>`;
          });
        pdiv.innerHTML = plist;
    });
}