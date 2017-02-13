function max(arr){
  if (arr.length == 0) {
    console.log("Empty array, no max value.");
    return;
  }
  var max = arr[0];
  for (var i = 1; i < array.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  console.log("Max value is:" + max);
}
