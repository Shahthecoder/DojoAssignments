function fancyarr(symbol){
  var arr = [ "James", "Jill", "Jane", "Jack" ];

  if (symbol){
    for (var i = 0; i < arr.length; i++) {
      console.log(i,symbol,arr[i])
    }
  }
  else{
    for(var i = 0; i < arr.length; i++){
      console.log(i + " ->",   arr[i])
    }
  }
}
fancyarr();
