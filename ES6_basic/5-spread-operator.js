export default function concatArrays(array1, array2, string) {
  const merge = [...array1, ...array2, ...string];
  return merge;
}
