function steps(n) {
  for (let i = 0; i < n; i++) {
    let line = "";
    for (let j = 0; j < n; j++) {
      j <= i ? (line += "#") : (line += " ");
    }
    console.log(line, line.length);
  }
}

console.log(steps(4));
 