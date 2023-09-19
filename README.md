# streamlit-llm-hackathon-2023


# Cloud Cost Saver App

The Cloud Cost Saver App is a Streamlit-based application that allows users to interact with a CSV dataset and query it using a language model powered by OpenAI's GPT-3.5 Turbo. Users can upload a CSV file, select from predefined queries, or enter custom queries to retrieve insights and recommendations related to optimizing cloud resources and cost-saving.

## Features

- Upload a CSV file to analyze.
- Select from predefined queries.
- Enter custom queries for more specific analysis.
- Retrieve recommendations to optimize cloud resources and reduce costs.
- Generate Terraform code templates based on the recommendations.
- View and reference previous responses.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/cloud-cost-saver-app.git
   cd cloud-cost-saver-app

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:

   ```bash
   streamlit run streamlit_app.py

Use the app by uploading a CSV file and interacting with the provided queries.

Usage
Upload a CSV File: Click on the "Upload a CSV file" button to select and upload a CSV dataset for analysis.

Select an Example Query: Choose from predefined queries in the dropdown list. The available queries include recommendations for optimizing cloud resources and generating Terraform code templates.

Enter Your Query: If you select "Other" in the query dropdown, a text input field will appear. Enter a custom query for more specific analysis.

Enter Your OpenAI API Key: You will need to provide your OpenAI API key in the text input field. Ensure that it starts with "sk-" and is valid.

Generate Response: Click the "Generate Response" button to submit your query and retrieve a response. The response will be displayed below.

View Previous Responses: All previous responses will be displayed in a list below the current response. You can reference and compare them.

Dependencies
Streamlit: Streamlit is used for building the interactive web application.

pandas: pandas is used for data manipulation and reading CSV files.

langchain: This package includes the language model and agent used for natural language processing tasks.

OpenAI GPT-3.5 Turbo: The language model provided by OpenAI powers the natural language understanding and generation capabilities of the app.
