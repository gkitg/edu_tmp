let paragraph = "Bob hit a ball, the hit BALL flew far after it was hit";

function fillArray(paragraph) {
  let regexp = /,/;
  let freq = {};
  let max = 0;

  paragraph = paragraph
    .replace(regexp, "")
    .toLowerCase()
    .split(" ");

  paragraph.forEach(word => {
    if (freq[word]) {
      freq[word]++;
    } else {
      freq[word] = 1;
    }

    if (freq[word] > max) {
      max = freq[word];
      result = word;
    }
  });

  return result;
}

console.log(fillArray(paragraph)); // hit
