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
