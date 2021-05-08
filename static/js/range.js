var slider = document.getElementById("slider");
var selector = document.getElementById("selector");
var SelectValue = document.getElementById("SelectValue");

SelectValue.innerHTML = slider.value;

slider.oninput = function(){
    SelectValue.innerHTML = this.value;
    selector.style.left = this.value + "%";
}

var slider2 = document.getElementById("slider2");
var selector2 = document.getElementById("selector2");
var SelectValue2 = document.getElementById("SelectValue2");

SelectValue2.innerHTML = slider2.value;

slider2.oninput = function(){
    SelectValue2.innerHTML = this.value;
    selector2.style.left = this.value + "%";
}

function noRooms(){
    const rooms = document.getElementById('slider2').value;

    localStorage.setItem('ROOMS', rooms);
    return;
}