# SQL Query Generator

This is a SQL query generator that utilizes the Google Gemini Pro API along with Streamlit. It allows you to easily generate SQL queries using data from the Gemini Pro API and visualize the results using Streamlit.

## Features

- Connects to the Google Gemini Pro API to retrieve data.
- Generates SQL queries based on selected data parameters.
- Visualizes query results using Streamlit.

## Prerequisites

Before running the SQL query generator, make sure you have the following prerequisites installed:

- Python 3.10
- Google Gemini Pro API credentials
- Streamlit

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/garunAMT/sql-query-generator.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Google Gemini Pro API credentials by following the instructions in the [Google Gemini Pro API documentation](https://docs.google.com/gemini-pro-api).

## Usage

1. Run the application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to access the SQL query generator.

3. Select the desired data parameters and click on the "Generate Query" button.

4. The generated SQL query will be displayed on the screen.

5. Copy the query and use it in your preferred SQL client to execute the query and retrieve the results.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
