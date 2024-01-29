<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI PowerPoint Creator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>AI PowerPoint Creator</h1>
        <textarea id="inputText" placeholder="Enter your lesson content here..."></textarea>
        <button onclick="generatePowerPoint()">Generate PowerPoint</button>
        <a id="downloadLink" style="display: none;" download="lesson_presentation.pptx">Download PowerPoint</a>
    </div>
    <script src="script.js"></script>
</body>
</html>


body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

textarea {
    width: 100%;
    height: 150px;
    margin-bottom: 15px;
}

button {
    background-color: #4caf50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

#downloadLink {
    color: #4caf50;
    text-decoration: none;
    display: block;
    margin-top: 10px;
}

function generatePowerPoint() {
    var inputText = document.getElementById("inputText").value;

    // Make an API request to your back-end for AI-powered PowerPoint generation
    // Assume the API returns a file path or data

    // For demonstration purposes, simulate a response
    var fakeResponse = { file_path: "path/to/lesson_presentation.pptx" };

    // Display download link
    var downloadLink = document.getElementById("downloadLink");
    downloadLink.href = fakeResponse.file_path;
    downloadLink.style.display = "block";
}


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    