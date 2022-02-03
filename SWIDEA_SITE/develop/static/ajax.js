let csrftoken = getCookie("csrftoken");
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const plus = document.querySelector(".plus"); // 우선 첫번째 +버튼만
const plus_href =
  plus.parentNode.previousElementSibling.previousElementSibling.getAttribute(
    "href"
  );
id = plus_href[plus_href.length - 1]; // 마지막 / 이후 숫자만 가져오도록 수정 필요
const url = `/edit/idea/${id}`;

plus.addEventListener("click", function () {
  let i = Number(document.querySelector(".interest").innerHTML); // interest-plus 연결짓도록 수정 필요
  fetch(url, {
    method: "post",
    headers: { "X-CSRFToken": csrftoken },
    body: JSON.stringify({ interest: i + 1 }),
  })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => console.log(error));
});
