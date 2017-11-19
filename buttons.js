var time;
var day;
var month;

document.getElementById("ALLDAY").click();
document.getElementById("ALLWK").click();
document.getElementById("ALLYR").click();

function changeTime(evt, tabName){
    var i, hour;
    hour = document.getElementsByClassName("time");
    for (i = 0; i<hour.length; i++){
        hour[i].className = hour[i].className.replace(" active", "");
    }
    time = tabName;
    changeMap(time, day, month);
    evt.currentTarget.className += " active";
}

function changeDay(evt, tabName){
    var i, wk;
    wk = document.getElementsByClassName("day");
    for (i = 0; i<wk.length; i++){
        wk[i].className = wk[i].className.replace(" active", "");
    }
    day = tabName;
    changeMap(time, day, month);
    evt.currentTarget.className += " active";
}

function changeMonth(evt, tabName){
    var i, mth;
    mth = document.getElementsByClassName("month");
    for (i = 0; i<mth.length; i++){
        mth[i].className = mth[i].className.replace(" active", "");
    }
    month = tabName;
    changeMap(time, day, month);
    evt.currentTarget.className += " active";
}

function changeMap(time, day, month){
    //document.getElementById("map").innerHTML = '<img class="photo" src="/photos/"' + time + '_' + day + '_' + month +'.png" width=100% >';
    document.getElementById("map").innerHTML = '<img class="photo" src="myimage.png" width=100% float="left">';
}