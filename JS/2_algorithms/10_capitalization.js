function capitalization(str) {
  const arr = str.split(" ").map(word => {
    word = word.split("");
    word[0] = word[0].toUpperCase();
    return word.join("");
  });

  return arr.join(" ");
}

console.log(capitalization("a short sentence"));
console.log(capitalization("a lazy fox"));
console.log(capitalization("look, it is working!"));
 