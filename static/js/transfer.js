function cargo(data){
    localStorage.setItem("ACAR", data);
}
document.getElementById('ai').innerHTML = localStorage.getItem('ACAR');

function date(){
    const date1 = document.getElementById('checkin').value;
    const date2 = document.getElementById('checkout').value;

    localStorage.setItem('DATE1', date1);
    localStorage.setItem('DATE2', date2);
    return;
}