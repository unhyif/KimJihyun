"use strict";

const rating = document.querySelectorAll(".stars");
rating.forEach((value) => {
  let ratingStars = "";
  for (let i = 0; i < Math.floor(value.innerText); i++) {
    ratingStars += '<i class="fas fa-star"></i>';
  }
  if (value.innerText % 1) {
    ratingStars += '<i class="fas fa-star-half"></i>';
  }
  value.innerHTML = ratingStars;
});

const select = document.querySelector("select");
if (!select) {
  return;
} else {
  select.addEventListener("change", function () {
    let value = select.options[select.selectedIndex].value;
    window.location.href = `http://127.0.0.1:8000/order_by_${value}`;
  });
} // need to learn query string
