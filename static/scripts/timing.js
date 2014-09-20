function updateTime(){
    document.getElementById('time').innerHTML = new Date();
    var t = setTimeout(function(){updateTime()},500)
}