/*function slots(quarters = 100, cap = 200){
    var res = 0;
    var pay = 0;
    while(quarters > 0 && quarters <= cap){
        quarters --;
        res = Math.ceil(Math.random()*100);
        if(res == 100){
            pay = Math.ceil(Math.random()*50) + 50;
            console.log("Congrats! you win", pay, "quarters!");
            quarters += pay;
        }
        console.log("Quarters remaining:", quarters);
    }
    if(quarters == 0){
        console.log("No more remaing quarters. Better luck next time.");
    }
    else{
        console.log("Congrats! You hit your goal of", cap);
    }
    console.log("Come back soon!");
}

slots();*/

var secret = prompt("What is the secret password?");
while ( secret !== "sesame" ) {
  secret = prompt("What is the secret password?");    
}
document.write("You know the secret password. Welcome.");
