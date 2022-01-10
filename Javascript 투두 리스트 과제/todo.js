const addBtn = document.querySelector(".add-btn");
const checkDeleteBtn = document.querySelector(".check-delete-btn");
const lastDeleteBtn = document.querySelector(".last-delete-btn");
const allDeleteBtn = document.querySelector(".all-delete-btn");

function handleAddBtn() {
  const content = document.querySelector(".add-container input").value;
  if (!content) {
    alert("내용을 입력해 주세요! 😮");
    return;
  }
  const tr = document.createElement("tr");
  tr.innerHTML = `<th scope="row"><input class="form-check-input" type="checkbox" /></th><td>${content}</td>`;
  document.querySelector("tbody").append(tr);
  document.querySelector(".add-container input").value = null;
}

function handleCheckDeleteBtn() {
  const checkedBoxes = document.querySelectorAll("tbody input:checked");
  if (checkedBoxes.length === 0) {
    alert("선택된 항목이 없어요 😅");
    return;
  }
  checkedBoxes.forEach((checkedBox) => {
    checkedBox.closest("tr").remove();
  });
}

function handleLastDeleteBtn() {
  const lastRow = document.querySelector("tbody tr:last-child");
  lastRow.remove();
}

function handleAllDeleteBtn() {
  const tbody = document.querySelector("tbody");
  while (tbody.hasChildNodes()) {
    tbody.removeChild(tbody.firstChild);
  }
}

addBtn.addEventListener("click", handleAddBtn);
checkDeleteBtn.addEventListener("click", handleCheckDeleteBtn);
lastDeleteBtn.addEventListener("click", handleLastDeleteBtn);
allDeleteBtn.addEventListener("click", handleAllDeleteBtn);
