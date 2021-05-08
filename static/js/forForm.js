$(document).ready(function(){
    const lol = $("#mainForm").clone();
    rom = parseInt( localStorage.getItem('ROOMS'));
    for(var i=1; i < rom; i++){
        $("#mainForm").append(lol.clone());
    }
    console.log(rom);
})