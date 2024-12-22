# Queue Manager Backend

This is the backend for the Queue Manager application. It provides a RESTful API for managing message queues, allowing users to add messages, retrieve messages, and view the list of available queues.

---

## Features

- **Add Messages**: Post messages to a named queue.
- **Retrieve Messages**: Get messages from a queue, with optional timeout handling.
- **View Queues**: List all available queues with the count of messages in each.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnnathBenhamou/queue-manager-backend.git
   cd queue-manager-backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Start the backend server:
   ```bash
   python server.py
   ```

2. The server will run on `http://127.0.0.1:5000`.

3. Use tools like `curl`, Postman, or the frontend application to interact with the backend.

---

## API Endpoints

### 1. Add a Message to a Queue
- **Endpoint**: `POST /api/<queue_name>`
- **Description**: Adds a message to the specified queue. If the queue does not exist, it is created automatically.
- **Request Body** (JSON):
  ```json
  {
    "message": "Your message here"
  }
  ```
- **Response**:
  ```json
  {
    "status": "Message added to queue"
  }
  ```

### 2. Get a Message from a Queue
- **Endpoint**: `GET /api/<queue_name>`
- **Description**: Retrieves the next message from the specified queue.
- **Query Parameters**:
  - `timeout` (optional): Timeout in milliseconds to wait for a message. Default is 10 seconds.
- **Responses**:
  - **200 OK**:
    ```json
    {
      "message": "Your message here"
    }
    ```
  - **204 No Content**: If no message is available in the queue after the timeout.

### 3. List All Queues
- **Endpoint**: `GET /queues`
- **Description**: Returns a list of all queues and their message counts.
- **Response**:
  ```json
  {
    "queue_name_1": 10,
    "queue_name_2": 5
  }
  ```

---

## Project Structure

```
queue-manager-backend/
├── server.py            # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
└── .gitignore           # Git ignore file
```

---

## Development

### Running the Server in Debug Mode
Start the Flask server with debugging enabled:
```bash
python server.py
```

---

## Dependencies

The backend uses the following Python packages:
- `flask`: For creating the REST API.
- `flask-cors`: For handling cross-origin requests.
- `queue`: Python's built-in queue module for managing in-memory queues.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Contributing

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

