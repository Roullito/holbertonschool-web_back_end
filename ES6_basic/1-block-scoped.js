export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true; // portée de bloc, non réassignable
    const task2 = false; // portée de bloc, non réassignable
  }

  return [task, task2];
}
