// Toggle Feature

const changeActiveTab = (event, tabID, tabImg) => {
  let element = event.target;
  while (element.nodeName !== "A") {
    element = element.parentNode;
  }
  let ulElement = element.parentNode.parentNode;
  let aElements = ulElement.querySelectorAll("li > a");
  let tabContents = document
    .getElementById("tab-id")
    .querySelectorAll(".tab-content > div");
  let imgContents = document
    .getElementById("tab-id")
    .querySelectorAll(".tab-img > img");
  for (let i = 0; i < aElements.length; i++) {
    aElements[i].classList.remove("text-headingColor");
    aElements[i].classList.remove("bg-gray2");
    aElements[i].classList.add("text-textColor");
    tabContents[i].classList.add("hidden");
    tabContents[i].classList.remove("block");
    imgContents[i].classList.add("hidden");
    imgContents[i].classList.remove("block");
  }
  element.classList.remove("text-textColor");
  element.classList.add("text-headingColor");
  element.classList.add("bg-gray2");
  document.getElementById(tabID).classList.remove("hidden");
  document.getElementById(tabID).classList.add("block");
  document.getElementById(tabImg).classList.remove("hidden");
  document.getElementById(tabImg).classList.add("block");
};

// Couter Animation

const counters = document.querySelectorAll(".value");
const speed = 200;

counters.forEach((counter) => {
    console.log("Chal raha he")
  const animate = () => {
    const value = +counter.getAttribute("last");
    const data = +counter.innerText;

    const time = value / speed;
    if (data < value) {
      counter.innerText = Math.ceil(data + time);
      setTimeout(animate, 1);
    } else {
      counter.innerText = value;
    }
  };

  animate();
});
