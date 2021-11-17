/* Scripts for adding and removing ingredients */
var x = 0;
const ingrArray = [];
const methodArray = [];

function addIngredient(ingrArray) {
    var ingTable = document.getElementById('ingredientTable');
    var ingRowNum = ingTable.rows.length;
    var ingRow = ingTable.insertRow(ingRowNum);
    var ingInput = document.getElementById('inputIngred').value;

    ingRow.insertCell(0).innerHTML += `<td class="col-sm-10">${ingInput}</td>`;
    ingRow.insertCell(1).innerHTML += `
        <td>
            <input class="btn btn-primary" type="button" id='btn${x}' value="Remove" onclick="delIngredient(this.parentNode)">
        </td>
    `;

    /* Adds ingredient to array */
    ingrArray.push(ingInput);
    x++;

    /* Update array carried through */
    document.getElementById('ingr-list').value = ingrArray;

    /* Resets input field */
    document.getElementById('inputIngred').value = "";

    console.log(ingrArray);
}

/* Delete selected ingredient table row and removes from array */
function delIngredient(selIngred) {
    /* Index of ingredient row to be deleted */
    var selRow = selIngred.parentNode.rowIndex;

    /* Deletes table row */
    document.getElementById('ingredientTable').deleteRow(selRow);

    /* Updates the array, removing selected row */
    ingrArray.splice(selRow, 1);

    console.log(ingrArray);
}


function addMethod(methodArray) {
    var metTable = document.getElementById('methodTable');
    var metRowNum = metTable.rows.length;
    var metRow = metTable.insertRow(metRowNum);
    var metInput = document.getElementById('inputMethod').value;

    metRow.insertCell(0).innerHTML += `<td class="col-sm-10">${metInput}</td>`;
    metRow.insertCell(1).innerHTML += `
        <td>
            <input class="btn btn-primary" type="button" id='btn${x}' value="Remove" onclick="delMethod(this.parentNode)">
        </td>
    `;

    /* Adds method to array */
    methodArray.push(metInput);
    x++;

    /* Update array carried through */
    document.getElementById('method-list').value = methodArray;

    /* Resets input field */
    document.getElementById('inputMethod').value = "";

    console.log(methodArray);
}

/* Delete selected ingredient table row and removes from array */
function delMethod(selMethod) {
    /* Index of ingredient row to be deleted */
    var selRow = selMethod.parentNode.rowIndex;

    /* Deletes table row */
    document.getElementById('methodTable').deleteRow(selRow);

    /* Updates the array, removing selected row */
    methodArray.splice(selRow, 1);

    console.log(methodArray);
}