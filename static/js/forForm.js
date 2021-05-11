$(document).ready(function(){
    const lol = $("#first-group").clone();
    rom = parseInt( localStorage.getItem('ROOMS'));
    for(var i=1; i < rom; i++){
        $("#first-group").append(lol.clone());
    }
    console.log(rom);
})