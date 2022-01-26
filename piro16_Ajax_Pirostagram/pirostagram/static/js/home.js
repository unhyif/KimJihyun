// Like

const requestLike = new XMLHttpRequest();
const onClickLike = (id) => {
  const post = document.querySelector(`.post[data-id="${id}"]`);

  let action;
  if (post.hasAttribute("data-liked")) {
    action = "minus";
    post.removeAttribute("data-liked");
  } else {
    action = "plus";
    post.setAttribute("data-liked", true);
  }

  const url = "/like/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(JSON.stringify({ id: id, action: action }));
};

const likeResHandler = () => {
  if (requestLike.status < 400) {
    const { id, action } = JSON.parse(requestLike.response);
    const heart = document.querySelector(`.post[data-id="${id}"] .heart`);
    const num = document.querySelector(`.post[data-id="${id}"] .num`);
    let hrt;
    let cnt;

    if (action === "plus") {
      hrt = "💖";
      cnt = Number(num.innerText) + 1;
    } else {
      hrt = "🤍";
      cnt = Number(num.innerText) - 1;
    }
    heart.innerText = hrt;
    num.innerText = cnt;
  }
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    likeResHandler();
  }
};

// Write a comment

const forms = document.querySelectorAll("form");
forms.forEach((value) => {
  const post_id = Number(value.getAttribute("data-id"));
  value.addEventListener("submit", (e) => {
    e.preventDefault(); // prevents reload, submits data but views.py does nothing
    writeComment(post_id);
  });
});

const requestWrite = new XMLHttpRequest();
const writeComment = (post_id) => {
  const form = document.querySelector(`form[data-id="${post_id}"]`);
  const author = form.querySelector(".form__author");
  const content = form.querySelector(".form__content");

  const url = "/write/";
  if (author.value && content.value) {
    // validity 검증 방법..?
    requestWrite.open("POST", url, true);
    requestWrite.setRequestHeader(
      "Content-Type",
      "application/x-www-form-urlencoded"
    );
    requestWrite.send(
      JSON.stringify({
        post_id: post_id,
        author: author.value,
        content: content.value,
      })
    );
    author.value = null;
    content.value = null;
  }
};

const writeResHandler = () => {
  if (requestWrite.status < 400) {
    const { post_id, comment_id, author, content } = JSON.parse(
      requestWrite.response
    );
    const comments = document.querySelector(
      `.post[data-id="${post_id}"] .comments`
    );

    const comment = document.createElement("div");
    comment.classList.toggle("comment");
    comment.classList.toggle("my-2");
    comment.setAttribute("data-id", comment_id);
    comment.innerHTML = `<span class="comment__author mx-3">${author}</span><span class="comment__content">${content}</span> <button class="btn btn-sm btn-danger" onclick="onClickDelete(${comment_id})">-</button>`;
    comments.append(comment);
  }
};

requestWrite.onreadystatechange = () => {
  if (requestWrite.readyState === XMLHttpRequest.DONE) {
    writeResHandler();
  }
};

// Delete a comment

const requestDelete = new XMLHttpRequest();
const onClickDelete = (id) => {
  const url = "/delete/";
  requestDelete.open("POST", url, true);
  requestDelete.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestDelete.send(JSON.stringify({ id: id }));
};

const deleteResHandler = () => {
  if (requestDelete.status < 400) {
    const { id } = JSON.parse(requestDelete.response);
    comment = document.querySelector(`.comment[data-id="${id}"]`);
    comment.remove();
  }
};

requestDelete.onreadystatechange = () => {
  if (requestDelete.readyState === XMLHttpRequest.DONE) {
    deleteResHandler();
  }
};
