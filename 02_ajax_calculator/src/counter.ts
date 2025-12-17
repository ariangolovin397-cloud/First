export function setupCounter(element: HTMLButtonElement) {
  let counter = 0;
  const setCounter = (count: number) => {
    counter = count
    element.innerHTML = `count is ${counter}`
  };
  // element.onclick = () => setCounter(counter + 1)
  element.addEventListener('click', () => {
    setCounter(counter + 1)
  });
  element.addEventListener('click', () => {
    console.log(counter)
  });
  setCounter(0);
}
