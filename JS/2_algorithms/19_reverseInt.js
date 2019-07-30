const int = -123;

function reverseInt(int) {
  strReverse = String(int)
    .split("")
    .reverse()
    .map(char => (char === "-" ? "" : char))
    .join("");

  console.log(strReverse);

  return Number(strReverse) * Math.sign(int);
}

console.log(reverseInt(int));
 