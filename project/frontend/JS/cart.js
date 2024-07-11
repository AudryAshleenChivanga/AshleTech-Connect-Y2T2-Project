// Example cart items (this would normally be dynamically generated)
const cartItems = [
    { id: 1, name: "Birth Control Pills", price: 10.00, quantity: 1 },
    { id: 2, name: "Condoms Pack", price: 5.00, quantity: 2 }
];

function updateCart() {
    const tbody = document.querySelector('#cart-table tbody');
    tbody.innerHTML = ''; // Clear current cart items
    let total = 0;

    cartItems.forEach(item => {
        const row = tbody.insertRow();
        row.insertCell(0).textContent = item.name;
        row.insertCell(1).textContent = `$${item.price.toFixed(2)}`;
        const qtyInput = document.createElement('input');
        qtyInput.type = 'number';
        qtyInput.value = item.quantity;
        qtyInput.min = 1;
        qtyInput.addEventListener('change', (e) => {
            item.quantity = parseInt(e.target.value);
            updateCart(); // Recalculate cart after quantity change
        });
        row.insertCell(2).appendChild(qtyInput);
        const totalItemPrice = item.price * item.quantity;
        row.insertCell(3).textContent = `$${totalItemPrice.toFixed(2)}`;
        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        removeBtn.addEventListener('click', () => {
            cartItems.splice(cartItems.indexOf(item), 1); // Remove item from array
            updateCart(); // Update cart display
        });
        row.insertCell(4).appendChild(removeBtn);

        total += totalItemPrice;
    });

    document.getElementById('total-price').textContent = total.toFixed(2);
}

