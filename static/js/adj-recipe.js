/* Scripts for adding and removing ingredients */
var x = 0;
const ingrArray = Array();
var ingJSON = {};

function addIngredient(ingrArray) {
    var table = document.getElementById('ingredient-list');
    var rowNum = document.getElementById('ingredient-list').rows.length;
    var row = table.insertRow(rowNum);

    var inputIngr = document.getElementById('inputIngred').value;

    row.insertCell(0).innerHTML += `<td class="col-sm-10">${inputIngr}</td>`;
    row.insertCell(1).innerHTML += `
        <td>
            <input class="btn btn-primary" type="button" id='btn${x}' value="Remove" onclick="delIngredient(this.parentNode)">
        </td>
    `;

console.log(inputIngr);

    /* Adds ingredient to array */
    ingrArray.push(inputIngr);
    x++;
    
    /* Resets input field */
    document.getElementById('inputIngred').value ="";
    document.getElementById('ingr-list').value = ingrArray;

    console.log(ingrArray);
}

function delIngredient(selIngred) {
    var selRow = selIngred.parentNode.rowIndex;
    console.log(selRow);

    document.getElementById('ingredient-list').deleteRow(selRow);

    ingrArray.splice(selRow, 1);
    
    document.getElementById('ingr-list').value = ingrArray;
    
    console.log(ingrArray);
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
    if (rowNum > '1') {
        var row = table.deleteRow(rowNum - 1);
        rowNum--;
    } else {
        alert('No step to remove')
    }
}