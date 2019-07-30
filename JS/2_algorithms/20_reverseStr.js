const str = "abcdefgh";

function first(str) {
  let reverse = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reverse += str[i];
  }

  return reverse;
}

function second(str) {
  return str
    .split("")
    .reverse()
    .join("");
}

function third(str) {
  let newStr = "";

  for (const letter of str) {
    newStr += letter;
  }

  return newStr;
}

console.log(first(str));
console.log(second(str));
console.log(third(str));
 