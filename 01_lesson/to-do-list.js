function newElement() {
    const inputValue = document.getElementById("myInput").value;
    const category = document.getElementById("categorySelect").value;

    if (inputValue === "") {
        alert("Ievadi tekstu!");
        return;
    }

    const li = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    const spanText = document.createElement("span");
    spanText.textContent = inputValue + "  (" + category + ")";
    spanText.className = "task-text";
    spanText.onclick = function () {
        checkbox.checked = !checkbox.checked;
        checkbox.onchange();
    };

    checkbox.onchange = function () {
        if (checkbox.checked) {
            spanText.classList.add("checked");
        } else {
            spanText.classList.remove("checked");
        }
    };
    const deleteBtn = document.createElement("span");
    deleteBtn.textContent = " ×";
    deleteBtn.className = "deleteBtn";

    deleteBtn.onclick = function (b_1) {
        console.log("dell", b_1);
        li.remove();
    };

    li.appendChild(checkbox);
    li.appendChild(spanText);
    li.appendChild(deleteBtn);


    document.getElementById("myUL").appendChild(li);

    document.getElementById("myInput").value = "";
}