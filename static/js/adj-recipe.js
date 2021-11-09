function addIngredient() {
    var table = document.getElementById('ingredient-list');
    var rowNum = document.getElementById('ingredient-list').rows.length;
    var row = table.insertRow(rowNum);
    var cell = row.insertCell(0);

    var inputIngr = document.getElementById('inputIngred').value;

    cell.innerHTML += `${inputIngr}`;
}

function delIngredient() {
    var table = document.getElementById("ingredient-list");
    var rowNum = table.rows.length;
    if(rowNum > '1'){
        var row = table.deleteRow(rowNum - 1);
        rowNum--;
    }
    else {
        alert('No ingredient to remove')
    }
}

