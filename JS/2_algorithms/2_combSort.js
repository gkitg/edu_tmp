let arr = [12, 2, 45, 6, 32, 357, 24, 6346, 123, 75];

function combSorting(arr) {
    let factor = 1.247;
    let gapFactor = arr.length / factor;

    while (gapFactor > 1) {
        let gap = Math.round(gapFactor);
        for (let i = 0, j = gap; j < arr.length; i++, j++) {
            if (arr[i] >= arr[j]) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }
        gapFactor = gapFactor / factor;
    }

    return arr;
}

console.log(combSorting(arr));
 