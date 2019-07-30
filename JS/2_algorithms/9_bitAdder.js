function adder(num1, num2) {
  for (let i = 0; num1[i] || num2[i]; i++) {
    if (!num1[i]) num1 = "0" + num1;
    if (!num2[i]) num2 = "0" + num2;
  }

  let p = 0;
  let s = [];

  for (let i = num2.length - 1; i >= 0; i--) {
    let a = num1[i];
    let b = num2[i];

    s[i + 1] = p ^ (b ^ a);
    p = (p & (a ^ b)) | (a & b);

    if (i === 0) s[i] = p;
  }

  return console.log(s.join(""), "=", parseInt(Number(s.join("")), 2));
}

adder("1010001010101", "101010");
adder("101010", "1010001010101");
 