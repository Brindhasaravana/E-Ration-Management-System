document.addEventListener("DOMContentLoaded", function () {
    loadShops();
    loadAssignedProducts();
    loadUsers();
});

// Function to add a shop user
function addShop() {
    let name = prompt("Enter Shopkeeper Name:");
    let email = prompt("Enter Email:");
    let city = prompt("Enter City:");
    let contact = prompt("Enter Contact Number:");
    let aadhar = prompt("Enter Aadhar Number:");

    if (name && email && city && contact && aadhar) {
        let shopTable = document.getElementById("shopTable");
        let row = shopTable.insertRow();
        row.innerHTML = `
            <td>${shopTable.rows.length}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${city}</td>
            <td>${contact}</td>
            <td>${aadhar}</td>
            <td><button onclick="editShop(this)">Edit</button></td>
            <td><button onclick="deleteRow(this)">Delete</button></td>
        `;
        saveData("shops", shopTable.innerHTML);
    }
}

// Function to edit a shop user
function editShop(button) {
    let row = button.parentElement.parentElement;
    let name = prompt("Edit Name:", row.cells[1].innerText);
    let email = prompt("Edit Email:", row.cells[2].innerText);
    let city = prompt("Edit City:", row.cells[3].innerText);
    let contact = prompt("Edit Contact Number:", row.cells[4].innerText);
    let aadhar = prompt("Edit Aadhar Number:", row.cells[5].innerText);

    if (name && email && city && contact && aadhar) {
        row.cells[1].innerText = name;
        row.cells[2].innerText = email;
        row.cells[3].innerText = city;
        row.cells[4].innerText = contact;
        row.cells[5].innerText = aadhar;
        saveData("shops", document.getElementById("shopTable").innerHTML);
    }
}

// Function to delete a row
function deleteRow(button) {
    let row = button.parentElement.parentElement;
    row.remove();
    saveData("shops", document.getElementById("shopTable").innerHTML);
}

// Function to add assigned products
function assignProduct() {
    let name = prompt("Enter User Name:");
    let email = prompt("Enter Email:");
    let mobile = prompt("Enter Mobile:");
    let product = prompt("Enter Product Name:");
    let qty = prompt("Enter Quantity:");

    if (name && email && mobile && product && qty) {
        let assignTable = document.getElementById("assignTable");
        let row = assignTable.insertRow();
        row.innerHTML = `
            <td>${assignTable.rows.length}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${mobile}</td>
            <td>${product} - ${qty}</td>
        `;
        saveData("assignedProducts", assignTable.innerHTML);
    }
}

// Function to add a user
function addUser() {
    let name = prompt("Enter User Name:");
    let email = prompt("Enter Email:");
    let city = prompt("Enter City:");
    let contact = prompt("Enter Contact Number:");

    if (name && email && city && contact) {
        let usersTable = document.getElementById("usersTable");
        let row = usersTable.insertRow();
        row.innerHTML = `
            <td>${usersTable.rows.length}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${city}</td>
            <td>${contact}</td>
            <td><button onclick="viewProducts()">View Products</button></td>
            <td><button onclick="editUser(this)">Edit</button></td>
            <td><button onclick="deleteRow(this)">Delete</button></td>
        `;
        saveData("users", usersTable.innerHTML);
    }
}

// Function to edit a user
function editUser(button) {
    let row = button.parentElement.parentElement;
    let name = prompt("Edit Name:", row.cells[1].innerText);
    let email = prompt("Edit Email:", row.cells[2].innerText);
    let city = prompt("Edit City:", row.cells[3].innerText);
    let contact = prompt("Edit Contact:", row.cells[4].innerText);

    if (name && email && city && contact) {
        row.cells[1].innerText = name;
        row.cells[2].innerText = email;
        row.cells[3].innerText = city;
        row.cells[4].innerText = contact;
        saveData("users", document.getElementById("usersTable").innerHTML);
    }
}

// Function to view products assigned to users
function viewProducts() {
    alert("Show assigned products (this can be improved with a table).");
}

// Function to save data in local storage
function saveData(key, data) {
    localStorage.setItem(key, data);
}

// Function to load saved data
function loadShops() {
    if (localStorage.getItem("shops")) {
        document.getElementById("shopTable").innerHTML = localStorage.getItem("shops");
    }
}

function loadAssignedProducts() {
    if (localStorage.getItem("assignedProducts")) {
        document.getElementById("assignTable").innerHTML = localStorage.getItem("assignedProducts");
    }
}

function loadUsers() {
    if (localStorage.getItem("users")) {
        document.getElementById("usersTable").innerHTML = localStorage.getItem("users");
    }
}
document.addEventListener("DOMContentLoaded", function () {
    loadShops();
    loadAssignedProducts();
    loadUsers();
    loadHistory();
});

// Function to add a shop user
function addShop() {
    let name = prompt("Enter Shopkeeper Name:");
    let email = prompt("Enter Email:");
    let city = prompt("Enter City:");
    let contact = prompt("Enter Contact Number:");
    let aadhar = prompt("Enter Aadhar Number:");

    if (name && email && city && contact && aadhar) {
        let shopTable = document.getElementById("shopTable");
        let row = shopTable.insertRow();
        row.innerHTML = `
            <td>${shopTable.rows.length}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${city}</td>
            <td>${contact}</td>
            <td>${aadhar}</td>
            <td><button onclick="editShop(this)">Edit</button></td>
            <td><button onclick="deleteRow(this)">Delete</button></td>
        `;
        saveData("shops", shopTable.innerHTML);
    }
}

// Function to assign a product to a user
function assignProduct() {
    let name = prompt("Enter User Name:");
    let email = prompt("Enter Email:");
    let mobile = prompt("Enter Mobile:");
    let product = prompt("Enter Product Name (wheat, sugar, kerosene, palm oil, rice):");
    let qty = parseInt(prompt("Enter Quantity to Assign:"));

    if (name && email && mobile && product && qty > 0) {
        let assignTable = document.getElementById("assignTable");
        let row = assignTable.insertRow();
        row.innerHTML = `
            <td>${assignTable.rows.length}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${mobile}</td>
            <td>${product}</td>
            <td>${qty}</td>
            <td><button onclick="removeAssignment(this)">Remove</button></td>
        `;
        saveData("assignedProducts", assignTable.innerHTML);
        addHistory(name, product, qty);
    }
}

// Function to remove an assigned product
function removeAssignment(button) {
    let row = button.parentElement.parentElement;
    row.remove();
    saveData("assignedProducts", document.getElementById("assignTable").innerHTML);
}

// Function to add history entry
function addHistory(user, product, qty) {
    let historyTable = document.getElementById("historyTable");
    let row = historyTable.insertRow();
    let date = new Date().toLocaleString();
    row.innerHTML = `
        <td>${historyTable.rows.length}</td>
        <td>${user}</td>
        <td>${product}</td>
        <td>${qty}</td>
        <td>${date}</td>
    `;
    saveData("history", historyTable.innerHTML);
}

// Function to add a user
function addUser() {
    let name = prompt("Enter User Name:");
    let email = prompt("Enter Email:");
    let city = prompt("Enter City:");
    let contact = prompt("Enter Contact Number:");

    if (name && email && city && contact) {
        let usersTable = document.getElementById("usersTable");
        let row = usersTable.insertRow();
        row.innerHTML = `
            <td>${usersTable.rows.length}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${city}</td>
            <td>${contact}</td>
            <td><button onclick="viewProducts('${name}')">View Products</button></td>
            <td><button onclick="editUser(this)">Edit</button></td>
            <td><button onclick="deleteRow(this)">Delete</button></td>
        `;
        saveData("users", usersTable.innerHTML);
    }
}

// Function to view assigned products for a user
function viewProducts(user) {
    alert("Showing assigned products for " + user + " (Functionality to be expanded).");
}

// Function to edit a user
function editUser(button) {
    let row = button.parentElement.parentElement;
    let name = prompt("Edit Name:", row.cells[1].innerText);
    let email = prompt("Edit Email:", row.cells[2].innerText);
    let city = prompt("Edit City:", row.cells[3].innerText);
    let contact = prompt("Edit Contact:", row.cells[4].innerText);

    if (name && email && city && contact) {
        row.cells[1].innerText = name;
        row.cells[2].innerText = email;
        row.cells[3].innerText = city;
        row.cells[4].innerText = contact;
        saveData("users", document.getElementById("usersTable").innerHTML);
    }
}

// Function to save data in local storage
function saveData(key, data) {
    localStorage.setItem(key, data);
}

// Function to load saved data
function loadShops() {
    if (localStorage.getItem("shops")) {
        document.getElementById("shopTable").innerHTML = localStorage.getItem("shops");
    }
}

function loadAssignedProducts() {
    if (localStorage.getItem("assignedProducts")) {
        document.getElementById("assignTable").innerHTML = localStorage.getItem("assignedProducts");
    }
}

function loadUsers() {
    if (localStorage.getItem("users")) {
        document.getElementById("usersTable").innerHTML = localStorage.getItem("users");
    }
}

function loadHistory() {
    if (localStorage.getItem("history")) {
        document.getElementById("historyTable").innerHTML = localStorage.getItem("history");
    }
}
