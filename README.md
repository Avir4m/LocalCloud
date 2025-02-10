# LocalCloud

LocalCloud is an open-source cloud storage solution developed using Python and the Flask framework. Designed for local network deployment, it enables users to manage and access their files seamlessly within their own infrastructure.

## Features

- **User Management**: Efficiently handle multiple user accounts with secure authentication mechanisms.
- **Local Hosting**: Deploy the application on your local network, ensuring data privacy and control.
- **File Management**: Upload, download, and organize files with an intuitive interface.

## Installation

### Prerequisites

- Ensure Python 3.12 or higher is installed on your system. You can download it from the [official Python website](https://www.python.org/).
- Ensure that you have `git` installed to clone the repository. You can download it from [here](https://git-scm.com/).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Avir4m/LocalCloud.git
   cd LocalCloud
   ```

2. **Install Required Libraries**:
   Install the dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Application**:
   - Open the `src/run.py` file and ensure the configuration is correct.
   - You can change the `host` and `port` for the local deployment. By default, it is set to run on `host="0.0.0.0"` and `port=8000`, making it accessible on your local network.
   
   To change these values, modify the `app.run()` line:
   ```python
   app.run(debug=True, host="0.0.0.0", port=8000)
   ```
   - Set the `host` to `127.0.0.1` (or leave it as `"0.0.0.0"` for local network access).
   - Set the `port` if you want to use a different one (default is `8000`).

4. **Run the Application**:
   After configuring the application, run it using:
   ```bash
   python src/run.py
   ```

## Usage

Once the application is running, access it via your web browser at `http://localhost:8000` or, if configured for local network access, at `http://<your-local-ip>:8000`.

From there, you can:
- Create user accounts
- Upload, download, and manage your files
- Enjoy your personal cloud storage!

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your proposed changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](https://github.com/Avir4m/LocalCloud/blob/main/LICENSE) file.

## Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/Avir4m/LocalCloud/issues).