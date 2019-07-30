function createArray(min, max, step) {
    let arr = [];
    let value = min;

    while (value <= max) {
        arr.push(value);
        value += step;
    }
    return arr;
}

function binSearch(arr, toFind) {
    if (!arr) return null;
    var first = 0;
    var last = arr.length - 1;
    while (first < last) {
        var mid = first + Math.floor((last - first) / 2);
        if (arr[mid] >= toFind) last = mid;
        else first = mid + 1;
    }
    if (arr[last] == toFind) return last;
    else return null;
}

function linearSearch(arr, num) {
    for (let i = 0; i < arr.length; i++) {
        if (num === arr[i]) {
            return i;
        }
    }
}

function doWork() {
    let count = 10000;
    let arr = createArray(0, 10000000, 1);
    let dateStart;

    dateStart = Date.now();
    for (let i = 0; i < count; i++) {
        let num = Math.floor(Math.random() * 10000000);

        binSearch(arr, num);
    }
    console.log(Date.now() - dateStart, "<- ms executed bin search");

    dateStart = Date.now();
    for (let i = 0; i < count; i++) {
        let num = Math.floor(Math.random() * 10000000);

        linearSearch(arr, num);
    }
    console.log(Date.now() - dateStart, "<- ms executed linear search");
}

doWork();
 