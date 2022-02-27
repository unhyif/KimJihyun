function addTodo() {
  const input = document.querySelector(".add-input");
  const content = input.value;

  if (!content) {
    alert("내용을 입력해 주세요! 😮");
    return;
  }

  const tr = document.createElement("tr");
  tr.innerHTML = `<th scope="row"><input class="form-check-input" type="checkbox" /></th><td>${content}</td>`;
  document.querySelector("tbody").append(tr);

  input.value = null;
}

function deleteCheckedTodo() {
  const checkedBoxes = document.querySelectorAll("tbody input:checked");
  if (checkedBoxes.length === 0) {
    alert("선택된 항목이 없어요 😅");
    return;
  }

  checkedBoxes.forEach((checkedBox) => {
    checkedBox.closest("tr").remove();
  });
}

function deleteLastTodo() {
  const lastRow = document.querySelector("tbody tr:last-child");
  lastRow.remove();
}

function deleteAllTodo() {
  const tbody = document.querySelector("tbody");
  while (tbody.hasChildNodes()) {
    tbody.removeChild(tbody.firstChild);
  }
}
