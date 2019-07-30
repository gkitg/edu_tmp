function vowels(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  let count = 0;

  for (const char of str.toLowerCase()) {
    for (const vowel of vowels) {
      if (char === vowel) count++;
    }
  }

  return count;
}

function vowels1(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  let count = 0;

  for (const char of str.toLowerCase()) {
    if (vowels.includes(char)) count++;
  }

  return count;
}

function vowels2(str) {
  const matches = str.match(/[aeiou]/gi);
  return matches ? matches.length : 0;
}

console.log(vowels2("Hi there"));
console.log(vowels2("Why do you ask?"));
console.log(vowels2("Why?"));
 