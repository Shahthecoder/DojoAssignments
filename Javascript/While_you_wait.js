function whileYouWait(){

var daysUntilMyBirthday = 31;

for (var i = daysUntilMyBirthday; i >= 0; i--){

if (i > 30){
  console.log("My birthday is so far away");
}

else if (i <= 30 && i > 5){
  console.log("The final count down begins!");
}

else if (i <= 5 && i > 0){
  console.log("Almost there,Can't wait!");
}

else{
  console.log("Happy birthday!!!");
}

}

}
whileYouWait();
