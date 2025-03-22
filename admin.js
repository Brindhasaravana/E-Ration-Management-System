// Admin Login with Dummy Email & Password
function adminLogin() {
    let email = document.getElementById("adminEmail").value;
    let password = document.getElementById("adminPassword").value;

    if (email === "admin@gmail.com" && password === "admin123") {
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid Credentials!");
    }
}

// Logout Function
function logout() {
    alert("Logging out...");
    window.location.href = "../homepage/index.html";
}

// Add Product
function addProduct() {
    let productName = document.getElementById("productName").value;
    let productMRP = document.getElementById("productMRP").value;
    let productQTY = document.getElementById("productQTY").value;

    if (productName === "" || productMRP === "" || productQTY === "") {
        alert("Fill all fields!");
        return;
    }

    let table = document.getElementById("productTable");
    let row = table.insertRow(-1);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(4);
    let cell6 = row.insertCell(5);

    let index = table.rows.length - 1;
    cell1.innerText = index;
    cell2.innerText = productName;
    cell3.innerText = productMRP;
    cell4.innerText = productQTY;
    cell5.innerHTML = `<button onclick="editProduct(this)">Edit</button>`;
    cell6.innerHTML = `<button onclick="deleteProduct(this)">Delete</button>`;
}

// Edit Product
function editProduct(btn) {
    let row = btn.parentNode.parentNode;
    let name = prompt("Edit Product Name", row.cells[1].innerText);
    let mrp = prompt("Edit MRP", row.cells[2].innerText);
    let qty = prompt("Edit Quantity", row.cells[3].innerText);

    row.cells[1].innerText = name;
    row.cells[2].innerText = mrp;
    row.cells[3].innerText = qty;
}

// Delete Product
function deleteProduct(btn) {
    let row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
}
