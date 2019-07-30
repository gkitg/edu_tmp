const word = "abba";

function first(word) {
  const length = word.length - 1;

  for (let i = 0; i <= length / 2; i++) {
    if (word[i] !== word[length - i]) return false;
  }
  return true;
}

function second(word) {
  const reversed = word
    .split("")
    .reverse()
    .join("");

  return reversed === word;
}

console.log(first(word));
console.log(second(word));
 