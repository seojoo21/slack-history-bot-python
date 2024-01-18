**How to Run the Python Codes with Virtual Environment:**

- Ensure that you have the `python3-venv` package installed. You can install it using `apt`:

    ```bash
    sudo apt-get install python3-venv
    ```

- Navigate to your project's directory in the terminal and create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

- Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

- With the virtual environment activated, use `pip` to install your project's dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

- Deactivate the virtual environment when you're done working on your project:

    ```bash
    deactivate
    ```