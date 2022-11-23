console.log("bakhangildin@icloud.com");

const preventScroll = (e) => {
  e.preventDefault();
  e.stopPropagation();
  return false;
};

const open_btn = document.querySelector(".open__modal");
const close_btn = document.querySelector(".close__modal");
const modal = document.querySelector("dialog");

open_btn.addEventListener("click", () => {
  document.body.classList.add("disable-scroll");
  modal.showModal();

  const form = document.querySelector("form");
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const form_url =
      "https://script.google.com/macros/s/AKfycbw39Pmkl9IUw2Y1y6h2n6HNeK2TTrL9E_EBcirbS-nDUtNpK6yPh6Gv-fMBytZIBBmvGg/exec";
    console.log(e.target);
    const url = `${form_url}?name=${e.target.name.value}&email=${e.target.email.value}&phone=${e.target.phone.value}&message=${e.target.message.value}`;
    window.open(encodeURI(url), "_blank");
  });
});

modal.addEventListener("click", (e) => {
  var rect = modal.getBoundingClientRect();
  var isInDialog =
    rect.top <= e.clientY &&
    e.clientY <= rect.top + rect.height &&
    rect.left <= e.clientX &&
    e.clientX <= rect.left + rect.width;
  if (!isInDialog) {
    document.body.classList.remove("disable-scroll");
    modal.close();
  }
});
close_btn.addEventListener("click", () => {
  document.body.classList.remove("disable-scroll");
  modal.close();
});

modal.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    document.body.classList.remove("disable-scroll");
    modal.close();
  }
});
