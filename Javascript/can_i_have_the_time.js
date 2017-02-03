var hour = 8;
var minute = 50;
var period = "AM";


if (minute > 30 && period == "AM") {
   console.log("It is almost", hour + 1, "in the morning");
}


var hour = 7;
var minute = 15;
var period = "PM";


if (minute < 30 && period == "PM") {
   console.log("It is just after", hour, "in the evening");
}
