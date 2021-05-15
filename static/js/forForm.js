$(document).ready(function(){
    const lol = $(".room").clone();
    rom = parseInt( localStorage.getItem('ROOMS'));
    for(var i=1; i < rom; i++){
        $(".new").append(lol.clone());
    }
    console.log(rom);
    e.preventDefault(); 
})