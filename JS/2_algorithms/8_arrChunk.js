function chunk1(arr, size) {
  const result = [];

  for (let i = 0, chunk = []; i < arr.length; i++) {
    chunk.push(arr[i]);

    if (chunk.length >= size || i === arr.length - 1) {
      result.push(chunk);
      chunk = [];
    }
  }
  return result;
}

console.log(chunk([1, 2, 3, 4, 5], 2));
 