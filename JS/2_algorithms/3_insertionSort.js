let arr = [54, 26, 93, 17, 77, 31, 44, 55, 20];

function insertionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let num = arr[i];
        for (var j = i - 1; j > -1 && arr[j] > num; j--) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = num;
    }

    return arr;
}

console.log(insertionSort(arr));
 