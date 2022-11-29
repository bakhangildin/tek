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

const forms = document.querySelectorAll("form");
forms.forEach((form, index) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const form_url =
      "https://script.google.com/macros/s/AKfycbypRpkOz2cyc6LnTYUD4S4docU_Q51I32lM5Qzhe2aIAjxB9PRiHnSCr5dbWQP465pv/exec";
    const url = `${form_url}?name=${e.target.name.value}&email=${e.target.email.value}&phone=${e.target.phone.value}&message=${e.target.message.value}`;
    window.open(encodeURI(url), "_blank");
  });
});
