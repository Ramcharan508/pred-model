document.getElementById('predictForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get input values
    const rdSpend = parseFloat(document.getElementById('rdSpend').value);
    const adminSpend = parseFloat(document.getElementById('adminSpend').value);
    const marketingSpend = parseFloat(document.getElementById('marketingSpend').value);

    // Validate input values
    if (isNaN(rdSpend) || isNaN(adminSpend) || isNaN(marketingSpend)) {
        alert("Please enter valid numbers.");
        return;
    }

    // Prepare data for sending to backend
    const inputData = {
        rdSpend: rdSpend,
        adminSpend: adminSpend,
        marketingSpend: marketingSpend
    };

    // Call the backend model using fetch
    fetch('http://127.0.0.1:5000/predict', {  // Change URL to your server's endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(inputData),
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.predictedProfit) {
            // Display predicted profit
            document.getElementById('profitValue').textContent = `$${data.predictedProfit.toFixed(2)}`;
        } else {
            alert("Failed to get prediction.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error occurred. Please try again.");
    });
});
