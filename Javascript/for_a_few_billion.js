function rewardfor30days(){}

var pay = 0.01;
var reward = 0;

for (var i=1; i <= 30; i++){
   console.log(pay);
   reward += pay;
   pay *= 2;

console.log(reward);
}
rewardfor30days();
// reward after 30 days

function daysto10000(){
  var pay = 0.01;
  var reward = 0
  var days=0;
  while(reward <= 10000){
    reward += pay;
    pay *= 2 ;
    days ++

  }
  console.log(days)
}

daysto10000();
// how many days until 10,000

function daystobillion(){
  var pay = 0.01;
  var reward = 0
  var days=0;
  while(reward <= 1000000000){
    reward += pay;
    pay *= 2 ;
    days ++

  }
  console.log(days)
}

daystobillion();
// days until a billion

function daysforinfinity(){

var pay = 0.01;
var reward = 0;
var day=0;
while(reward<Infinity){
   reward += pay;
   pay *= 2;
   day ++;
 }

console.log("it takes",day,"days to infinity dollars");
}

daysforinfinity();
// This is how many days it takes to infinity dollars
