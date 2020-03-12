/*var age=5;
while(age<10){
    console.log("your age is less than 10");
    age++;
}
document.write("You are now over 10");
*/

/*for (age=0; age<10; age++){
    console.log("your age is less than 10");
}
document.write("You are now over 10");
*/
/*
for (i = 0; i < 10; i++) {
    if (i === 5 || i === 3) {
        continue;
    }
    console.log(i);
    if (i === 7) {
        break;
    }
}
console.log("I have broken out of the loop");

var links = document.getElementsByTagName("a");
for(i=0; i<links.length; i++){
    links[i].className="link-"+i;
}
*/

function getAverage(a,b){
var average=(a+b)/2;
console.log(average);
return average
}
var myResult=getAverage(7,8);
console.log("the average is " + myResult);
