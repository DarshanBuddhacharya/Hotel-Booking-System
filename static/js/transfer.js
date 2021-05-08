function cargo(data){
    localStorage.setItem("ACAR", data);
}
document.getElementById('ai').innerHTML = localStorage.getItem('ACAR');

function ver(data){
    localStorage.setItem("VERS", data);
    document.getElementById("ver").innerHTML = localStorage.getItem('VERS');
}

function date(){
    const date1 = document.getElementById('checkin').value;
    const date2 = document.getElementById('checkout').value;

    localStorage.setItem('DATE1', date1);
    localStorage.setItem('DATE2', date2);
    return;
}

window.onload = function(){
    
    document.getElementById("datetimepicker1").innerHTML = localStorage.getItem('DATE1');
    document.getElementById("datetimepicker11").innerHTML = localStorage.getItem('DATE2');
}