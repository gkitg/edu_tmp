let arr = [12, 2, 45, 6, 32, 357, 24, 6346, 123, 75];

function selectionSort(arr) {
    let min = 0;
    for (let i = 0; i < arr.length; i++) {
        min = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] <= arr[min]) min = j;
        }
        let temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
    return arr;
}

console.log(selectionSort(arr));
 