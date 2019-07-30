function fizzBuzz(n) {
  for (let i = 1; i <= n; i++) {
    str = "";
    if (i % 3 === 0) str += "fizz";
    if (i % 5 === 0) str += "buzz";

    console.log(str ? str : i);
  }
}

fizzBuzz(30);
 