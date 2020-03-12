for(var i=1; i<256; i++){
    console.log(i);
    }

function go(){
    alert("hi");
    alert("hey there");
}
go();

function go(name,age){
    if (age<20){
        return name +"!";
    }
    else{
        return name;
    }
}
alert(go("will", "19"));