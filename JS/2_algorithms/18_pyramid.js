function pyramid(n) {
  const mid = Math.floor(n - 0.5);

  for (let i = 0; i < n; i++) {
    let line = "";

    for (let j = 0; j <= 2 * n - 1; j++) {
      if (mid - i <= j && mid + i >= j) {
        line += "#";
      } else {
        line += " ";
      }
    }
    console.log(line, line.length);
  }
}

console.log(pyramid(4));
 