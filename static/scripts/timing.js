function updateTime(){
	d = new Date()
	// d.format()
    document.getElementById('time').innerHTML = "Current Time: ".concat(d);
    var t = setTimeout(function(){updateTime()},500)
}

var txt = ""
function setText(val){
	txt = val
}

function updateText(){
    document.getElementById('txt').innerHTML = txt;
}