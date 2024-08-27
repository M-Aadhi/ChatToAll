# ChatToAll

## Overview

**ChatToAll** is a simple web-based chat application that allows users to send and view messages in real-time. The application is built using Flask for the backend and a basic HTML/CSS frontend. All messages are stored in a `chatlog.txt` file, which serves as the application's data storage.

## Features

- **Real-time Messaging:** Users can send and view messages instantly.
- **Persistent Storage:** Messages are saved in a text file, ensuring they are retained even after the server is restarted.
- **Simple Interface:** The application provides an easy-to-use interface with minimal distractions.

## Project Structure

- **`app.py`:** The main Flask application file that handles routing and message processing.
- **`templates/`:** Contains the HTML files for rendering the frontend.
- **`static/`:** Holds the CSS files for styling the application.
- **`chatlog.txt`:** Stores all chat messages.
- **`README.md`:** Project documentation.

## Installation

To run this project locally, follow these steps:

1. **Clone this repository:**

    ```bash
    git clone https://github.com/M-Aadhi/chatToAll.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd chattoall
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Access the application:**

    Open your web browser and navigate to `http://localhost:5000`.

## Usage

- **Sending Messages:** Type your message in the input box and press enter to send it.
- **Viewing Messages:** All messages are displayed in the chat window, updated in real-time.
- **Clearing Messages:** Messages can be cleared by restarting the server, which will reset the `chatlog.txt` file.

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
