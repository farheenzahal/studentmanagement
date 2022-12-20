
var pass1=document.getElementById("pass1");
var pass2=document.getElementById("pass2");

function validpass(){
    var passl =pass1.value.length;
    if ( passl >=8 & passl <=16){
        pass1.className="success";
        document.getElementById("text").innerHTML="";

    }else{
        pass1.className="error";
        document.getElementById("submit").disabled=true;
        // document.getElementById("text").innerHTML="password length must be greater than 8 characters and not exceed 15";
    }
 }


 function validpassconfirm(){
    var pass=pass1.value;
    var passc=pass2.value;
    if(pass == passc){
        pass2.className="success";
        document.getElementById("text").innerHTML="";
        document.getElementById("submit").disabled=false;

    }else{
      
        document.getElementById("submit").disabled=true;
        pass2.className="error";
        document.getElementById("text").innerHTML="password did not match";
    }
 }
document.getElementById("submit").disabled=true;