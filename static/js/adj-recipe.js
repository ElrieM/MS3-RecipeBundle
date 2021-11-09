
/* Scripts for adding and removing ingredients */
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

/* Scripts for adding and removing method steps */
function addMethod() {
    var table = document.getElementById('method-list');
    var rowNum = document.getElementById('method-list').rows.length;
    var row = table.insertRow(rowNum);
    var cell = row.insertCell(0);

    var inputStep = document.getElementById('inputMethod').value;

    cell.innerHTML += `${inputStep}`;
}

function delMethod() {
    var table = document.getElementById("method-list");
    var rowNum = table.rows.length;
    if(rowNum > '1'){
        var row = table.deleteRow(rowNum - 1);
        rowNum--;
    }
    else {
        alert('No step to remove')
    }
}
