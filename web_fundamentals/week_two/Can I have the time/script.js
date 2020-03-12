/*var HOUR= 8;
var MINUTE= 50;
var PERIOD="AM";
var str= "It's";

if(MINUTE > 30){
    str+= " almost " +(HOUR +1)
}else{
    str+= " just after " + HOUR
}

if(PERIOD== "PM"){
str+= " in the evening "
} else{
str+= " in the morning "
}
console.log(str);

var HOUR=7;
var MINUTE=15;
var PERIOD="PM"
str="It's"

if(MINUTE >30){
    str+=" almost " +(HOUR+1)
}else{
    str+=" just after "+ HOUR
}
 if(PERIOD=="PM"){
     str+=(" in the evening ")
 } else{
     str+=" in the morning "
 }
 console.log(str)*/
 function sum_even(arr){
     var sum=0;
     for(var i=2; i<128; i++){
         if(i%2===0){
             sum=sum+i;
         }
     }
     return sum;
 }

 