let arr = [1, 2, 5, 6, 8, 10, 12, 15, 19, 25, 28];

function binarySearch(arr, num) {
    let min = 0;
    let max = arr.length - 1;
    let mid = 0;

    while (min <= max) {
        mid = Math.floor((max + min) / 2);

        if (arr[mid] === num) return mid;
        if (arr[mid] > num) max = mid - 1;
        if (arr[mid] < num) min = mid + 1;
    }
}

// Test
for (let i = 0; i < arr.length; i++) {
    console.log(binarySearch(arr, arr[i]));
}
 