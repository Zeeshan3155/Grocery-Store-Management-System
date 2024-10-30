let rowIndex = 1
function addRow() {
    const row = `
        <tr>
            <td>
                <select class="form-control" id="product-select" name="product_${rowIndex}" required>
                    <option></option>
                    ${products.map(p => `<option value="${p.id}" data-price="${p.price}">${p.name}</option>`).join('')}
                </select>
            </td>
            <td>
                <input type="float" class="form-control quantity" placeholder=" " oninput="calculateTotal(this)" name="quantity_${rowIndex}" required>
            </td>
            <td>
                <input type="number" class="form-control price" placeholder=" " name="price_${rowIndex}" readonly>
            </td>
            <td>
                <input type="number" class="form-control total" placeholder=" " name="total_${rowIndex}" readonly>
            </td>
            <td>
                <button type="button" class="btn btn-danger" onclick="removeRow(this)">Remove</button>
            </td>
        </tr>
    `;
    document.getElementById('orderRows').insertAdjacentHTML('beforeend', row);
    rowIndex++;
    reinitializeSelect2();
    $('#orderRows tr:last select').select2();
}

function reinitializeSelect2(){
    let newRow = $('#info-table tr:last').clone();
    newRow.find('select').select2();
}

function removeRow(btn) {
    const row = btn.closest('tr');
    row.parentNode.removeChild(row);
}

function calculateTotal(input) {
    const row = input.closest('tr');
    const price = row.querySelector('#product-select').selectedOptions[0].getAttribute('data-price') || 0;
    const quantity = row.querySelector('.form-control.quantity').value || 0;
    row.querySelector('.form-control.price').value = parseFloat(price)
    total = price*quantity;
    row.querySelector('.form-control.total').value = parseFloat(total.toFixed(2)); // Assuming total is just the price for simplicity
    updateGrandTotal();
    }

function updateGrandTotal() {
    const totals = document.querySelectorAll('.total');
    let grandTotal = 0;
    totals.forEach(totalInput => {
        grandTotal += parseFloat(totalInput.value) || 0;
    });
    document.getElementById('grandTotal').value = grandTotal.toFixed(2);
}