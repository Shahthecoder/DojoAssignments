function x (arr, y) {
	var count = 0;
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] > y) {
			count++;
		}
	}
	return count;
}
console.log(x([1, 2, 3, 4, 5, 6, 7, 8, 9,  10], 5));
