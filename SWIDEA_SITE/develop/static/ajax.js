const requestInterest = new XMLHttpRequest();
const onClickInterest = (id, type) => {
  const url = "/interest/";
  requestInterest.open("POST", url, true);
  requestInterest.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestInterest.send(JSON.stringify({ id: id, type: type }));
};

const interestResHandler = () => {
  if (requestInterest.status < 400) {
    const { id, type } = JSON.parse(requestInterest.response);
    const interest = document.querySelector(
      `.object[data-id="${id}"] .interest`
    );
    let num;

    if (type === "plus") {
      num = Number(interest.innerText) + 1;
    } else {
      num = Number(interest.innerText) - 1;
    }
    interest.innerText = num;
  }
};

requestInterest.onreadystatechange = () => {
  if (requestInterest.readyState === XMLHttpRequest.DONE) {
    interestResHandler();
  }
};
