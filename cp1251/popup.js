const observerCallback = (entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    }
  });
};
const observerOptions = {};
observer = new IntersectionObserver(observerCallback, observerOptions);
document.querySelectorAll(".hidden").forEach((el) => {
  observer.observe(el);
});
