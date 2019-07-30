let testCase1 = "()";
let testCase2 = "()[]{}";
let testCase3 = "(|";
let testCase4 = "(|)]";
let testCase5 = "{[]}";

function isCorrect(str) {
    let stack = [];
    for (let i = 0; i < str.length; i++) {
        if (str[i] === "[" || str[i] === "(" || str[i] === "{") {
            stack.push(str[i]);
        } else {
            if (stack.length === 0) {
                return false;
            }
            let top = stack.pop();
            if (top === "[" && str[i] !== "]") return false;
            if (top === "(" && str[i] !== ")") return false;
            if (top === "{" && str[i] !== "}") return false;
        }
    }
    return stack.length === 0 ? true : false;
}

console.log(isCorrect(testCase1)); // true
console.log(isCorrect(testCase2)); // true
console.log(isCorrect(testCase3)); // false
console.log(isCorrect(testCase4)); // false
console.log(isCorrect(testCase5)); // true
 