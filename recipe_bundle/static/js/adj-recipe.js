/* jshint esversion: 6 */

/* Scripts for adding and removing ingredients */
var x = 0;
var ingrArray = [];
var methodArray = [];
var ingTable = document.getElementById('ingredientTable');

function addIngredient(ingrArray) {
    var ingRowNum = ingTable.rows.length;
    var ingRow = ingTable.insertRow(ingRowNum);
    var ingInput = document.getElementById('inputIngred').value;

    ingRow.insertCell(0).innerHTML += `<td class="col-sm-10">${ingInput}</td>`;
    ingRow.insertCell(1).innerHTML += `
        <td>
        <button class="btn btn-link" type="button" onclick="editIngredient(this.parentNode)"><i class="fas fa-edit"></i></button>
        <button class="btn btn-link" onclick="delIngredient(this.parentNode)"><i class="fas fa-trash-alt"></i></button>
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
    ingTable.deleteRow(selRow);

    /* Updates the array, removing selected row */
    ingrArray.splice(selRow, 1);

    console.log(ingrArray);
}

/* Edit selected ingredient table row */
function editIngredient(selIngred) {
    /* Index of ingredient row to be deleted */
    var selRow = selIngred.parentNode.rowIndex;
    var ingInput = document.getElementById('inputIngred').value;
    
    ingrList = document.getElementById('ingr-list').value;
    console.log(ingrList);
    
    var ingrArray = ingrList.split(";");
    console.log(selRow);
    console.log(ingrArray);

    document.getElementById('inputIngred').value = ingrArray[selRow];
    /* Update value in table row */
    document.getElementById('ingredientTable');

    /* Updates the array, removing selected row */
    ingrArray[selRow] = ingInput;

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
            <input class="btn btn-primary" type="button" value="Remove" onclick="delMethod(this.parentNode)">
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

/* Edit selected method table row */
function editMethod(selMethod) {
    /* Index of method row to be deleted */
    var selRow = selMethod.parentNode.rowIndex;
    var metInput = document.getElementById('inputMethod').value;
    
    methodList = document.getElementById('method-list').value;
    console.log(methodList);
    var methodArray = methodList.split(";");
    console.log(selRow);
    console.log(methodArray);

    document.getElementById('inputMethod').value = methodArray[selRow];

    /* Update value in table row */
    document.getElementById('methodTable');

    /* Updates the array, removing selected row */
    methodArray[selRow] = metInput;

    console.log(methodArray);
}