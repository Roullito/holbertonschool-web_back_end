export default function appendToEachArrayValue(array, appendString) {
    let i = 0;
    for (let val of array) {
    array[i] = appendString + val;
    i++;
  }

  return array;
}
