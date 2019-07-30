const str = "abcccdd";

function maxChar(str) {
  const obj = {};
  let max = 0;
  let result = "";

  for (let char of str) {
    obj[char] = obj[char] + 1 || 1;
    if (obj[char] > max) {
      max = obj[char];
      result = char;
    }
  }

  return result;
}

console.log(maxChar(str));
 