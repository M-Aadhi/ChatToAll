# ChatToAll

## Overview

**ChatToAll** is an enhanced web-based chat application that allows users to send and view messages in real-time. The application is built using Flask for the backend and a responsive HTML/CSS frontend. All messages are stored in a `chatlog.json` file, which serves as the application's data storage.

## Features

- **Real-time Messaging:** Users can send and view messages instantly.
- **Persistent Storage:** Messages are saved in a JSON file, ensuring they are retained even after the server is restarted.
- **Responsive Interface:** The application provides a dynamic and responsive interface suitable for both desktop and mobile devices.
- **Improved UI:** Enhanced user interface with better layout and styles.

## Project Structure

- **`app.py`:** The main Flask application file that handles routing and message processing.
- **`templates/`:** Contains the HTML files for rendering the frontend.
- **`static/`:** Holds the CSS and JavaScript files for styling and frontend logic.
    - **`styles.css`:** Styles the application with a dynamic and responsive design.
    - **`app.js`:** Handles frontend logic and API calls.
- **`data/chatlog.json`:** Stores all chat messages in JSON format.
- **`README.md`:** Project documentation.
- **`requirements.txt`:** Lists the project dependencies.
- **`LICENSE`:** License information.
- **`.gitignore`:** Specifies files to be ignored by Git.

## Installation

To run this project locally, follow these steps:

1. **Clone this repository:**

    ```bash
    git clone https://github.com/M-Aadhi/chatToAll.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd chatToAll
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

- **Sending Messages:** Type your message in the input box and press enter or click the "Send" button to send it.
- **Viewing Messages:** All messages are displayed in the chat window, updated in real-time.
- **Clearing Messages:** Messages can be cleared by deleting the `data/chatlog.json` file or implementing a clear feature.

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
