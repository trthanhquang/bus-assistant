function updateTime(){
    document.getElementById('time').innerHTML = new Date();
    var t = setTimeout(function(){updateTime()},500)
}

var txt = ""
function setText(val){
	txt = val
}

function updateText(){
    document.getElementById('txt').innerHTML = txt;
}