function numsOnly (arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (typeof(arr[i]) === "number") {
            newArr.push(arr[i])
        }
    }
    return newArr;
}

console.log(numsOnly(["hello", 1, "coding", 2, "dojo", 3]));

function removeNums(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (typeof(arr[i]) === "number") {
            arr.splice(i, 1);
        }
    }
    return arr;
}

console.log(removeNums(["hello", 1, "coding", 2, "dojo", 3]));