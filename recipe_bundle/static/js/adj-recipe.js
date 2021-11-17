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
    
    /* Resets input field */
    document.getElementById('inputIngred').value ="";

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