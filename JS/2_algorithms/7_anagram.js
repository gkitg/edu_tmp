function anagrams(strA, strB) {
  const regExp = /\W/g;
  strA = strA
    .toLowerCase()
    .replace(regExp, "")
    .split("")
    .sort()
    .join("");

  strB = strB
    .toLowerCase()
    .replace(regExp, "")
    .split("")
    .sort()
    .join("");

  console.log(strA, strB);

  return strA === strB;
}

console.log(anagrams("Hi there", "Bye there"));
 