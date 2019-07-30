let testCase1 = "abba";
let testCase2 = "a Bb  a";
let testCase3 = "bba";
let testCase4 = "aba";

function isPalindrom(s) {
    let regex = /\s/g;

    s = s.replace(regex, "").toLowerCase();

    for (let i = 0; i < s.length / 2; i++) {
        if (s[i] !== s[s.length - 1 - i]) {
            return false;
        }
    }
    return true;
}

console.log(isPalindrom(testCase1)); // true
console.log(isPalindrom(testCase2)); // true
console.log(isPalindrom(testCase3)); // false
console.log(isPalindrom(testCase4)); // true
 