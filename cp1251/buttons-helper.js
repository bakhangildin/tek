const header = document.querySelector(".header");
let headerHeight = header.offsetHeight;
document
  .querySelector(":root")
  .style.setProperty("--header-height", `${-headerHeight + 1}px`);

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});
const isActive = (el) => {
  return el.getBoundingClientRect()["y"] - window.innerHeight;
};
let menu_buttons = [...document.querySelectorAll(".header__menu-link")];
const paintButtons = () => {
  let sections = [...document.querySelectorAll("section")].map((el) => {
    return el.getBoundingClientRect()["y"] - window.innerHeight;
  });
  let current = sections.length - sections.filter((el) => el > 0).length - 1;
  menu_buttons.forEach((button) => {
    button.classList.remove("active");
  });
  menu_buttons[current].classList.add("active");
};
paintButtons();
window.addEventListener("scroll", paintButtons);

document
  .querySelector("#link-to-other-patents")
  .addEventListener("click", (e) => {
    window.location.href = "all_patents.html";
  });
