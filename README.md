# My Streamlit App

This is a simple Streamlit application designed to demonstrate the capabilities of Streamlit for building interactive web applications.

## Project Structure

```
my-streamlit-app
├── src
│   ├── app.py          # Main entry point of the Streamlit application
│   └── utils
│       └── helpers.py  # Utility functions for the application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-streamlit-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/app.py
```
This will start the Streamlit server, and you can view the app in your web browser at `http://localhost:8501`.

## Deployment

To deploy the Streamlit application on a custom domain, follow these steps:

1. Choose a hosting service that supports Streamlit applications (e.g., Streamlit Sharing, Heroku, or AWS).
2. Configure your domain settings to point to the hosting service.
3. Follow the hosting service's instructions for deploying a Streamlit app.
4. Update your DNS records to link your custom domain to the deployed application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.