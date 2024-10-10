async function submitForm(event) {
    event.preventDefault(); // Prevent the default form submission
    
    // Get the video link from the input field
    const link = document.getElementById('videoLink').value;

    // Send a POST request to the FastAPI server
    const response = await fetch('http://127.0.0.1:8000/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `link=${encodeURIComponent(link)}` // URL-encoded form data
    });
    
    // Handle the response
    const data = await response.json();
    if (response.ok) {
        document.getElementById('result').innerText = 'Downloaded Successfully!!!';
        document.getElementById('result').style.color = "#28a745"; // Green success message
    } else {
        document.getElementById('result').innerText = `Error: ${data.error}`;
        document.getElementById('result').style.color = "#e74c3c"; // Red error message
    }
}
