document.addEventListener("DOMContentLoaded", function() {
    let assignedProducts = [
        { id: 1, name: "Wheat", mrp: 50, quantity: 100 },
        { id: 2, name: "Sugar", mrp: 40, quantity: 80 },
        { id: 3, name: "Rice", mrp: 60, quantity: 90 },
    ];

    let tableBody = document.getElementById("assigned-products");

    assignedProducts.forEach((product, index) => {
        let row = `<tr>
            <td>${index + 1}</td>
            <td>${product.name}</td>
            <td>${product.mrp}</td>
            <td>${product.quantity}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
});
function searchUser() {
    let mobile = document.getElementById("searchUser").value;
    let userDetails = document.getElementById("userDetails");
    
    // Dummy user data
    let users = {
        "9876543210": { name: "John Doe", email: "john@example.com" },
        "9123456789": { name: "Jane Smith", email: "jane@example.com" }
    };

    if (users[mobile]) {
        userDetails.innerHTML = `<p>Name: ${users[mobile].name}</p>
                                 <p>Email: ${users[mobile].email}</p>`;
        document.getElementById("assignProductSection").style.display = "block";
    } else {
        userDetails.innerHTML = "<p>User not found</p>";
    }
}

function assignProduct() {
    let product = document.getElementById("productSelect").value;
    let quantity = document.getElementById("quantity").value;
    alert(`Assigned ${quantity} units of ${product} to user.`);
}
document.addEventListener("DOMContentLoaded", function() {
    let shopUsers = [
        { id: 1, name: "stark", mobile: "9876543210", city: "chennai", product: "Wheat", qty: "5kg", date: "2025-03-20" },
    ];

    let tableBody = document.getElementById("shopUsers");
    shopUsers.forEach((user, index) => {
        let row = `<tr>
            <td>${index + 1}</td>
            <td>${user.name}</td>
            <td>${user.mobile}</td>
            <td>${user.city}</td>
            <td>${user.product}</td>
            <td>${user.qty}</td>
            <td>${user.date}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
});
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("total-customers").textContent = "15"; // Replace with actual data
    document.getElementById("total-products").textContent = "20"; 
    document.getElementById("total-assigned").textContent = "10";
});

