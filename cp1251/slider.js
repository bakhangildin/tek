const addDots = () => {
  let slides = Array.from(document.getElementsByClassName("mySlides"));
  let dots = document.querySelector(".dots");
  for (let i = 0; i < slides.length; i++) {
    const newDot = document.createElement("span");
    newDot.className = "dot";
    // newDot.onclick = currentSlide(i + 1);
    dots.append(newDot);
  }
};
addDots();

let slideIndex = 1;
showSlides(slideIndex);

function currentSlide(n) {
  showSlides((slideIndex = n));
}

const updateDots = () => {
  let dots = document.querySelectorAll(".dot");
  for (let i = 0; i < dots.length; i++) {
    dots[i].addEventListener("click", (e) => {
      currentSlide(i + 1);
    });
  }
};
updateDots();

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
