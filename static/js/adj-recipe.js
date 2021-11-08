function add_ingredient(inputIngred) {
    var table = document.getElementById('ingredient-list');
    var rowNum = table.rows.length;
    var row = table.insertRow(rowNum);
    var rowId = "ingr" + (rowNum);
    var ingr = inputIngred.value;

    row.innerHTML = `
            <td id="${rowId}">${ingr}</td>
            <td class="col-sm-1">
                <button class="btn btn-primary" type="button" id="remove-ingredient"
                    onclick="del_ingredient(this.id)">
                    <i class="fas fa-minus"></i>
                </button>
            </td>
    `;
}