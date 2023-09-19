import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

# Page title
st.set_page_config(page_title='🦜🔗 Cloud cost saver App')
st.title('🦜🔗 Cloud cost saver App')

# Load CSV file
def load_csv(input_csv):
  df = pd.read_csv(input_csv)
  with st.expander('See DataFrame'):
    st.write(df)
  return df

# Generate LLM response
def generate_response(csv_file, input_query, responses):
  llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key=openai_api_key)
  df = load_csv(csv_file)
  # Create Pandas DataFrame Agent
  agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
  # Perform Query using the Agent
  response = agent.run(input_query)
  responses.append(response)  # Append the response to the list of responses
  return responses

# Input widgets
uploaded_file = st.file_uploader('Upload the cloud bill CSV file', type=['csv'])
question_list = [
  'Provide recommendations to optimize the resources and save the cloud cost bill',
  'Generate Terraform code template based on the recommendations',
  'Generate Terraform documentation based on the generated code',
  'Other']
query_text = st.selectbox('Select an example query:', question_list, disabled=not uploaded_file)
openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))

# Initialize responses list
responses = []

# App logic
if query_text == 'Other':
  query_text = st.text_input('Enter your query:', placeholder='Enter query here ...', disabled=not uploaded_file)
if not openai_api_key.startswith('sk-'):
  st.warning('Please enter your OpenAI API key!', icon='⚠')
if openai_api_key.startswith('sk-') and (uploaded_file is not None):
  if st.button('Generate Response'):
    responses = generate_response(uploaded_file, query_text, responses)

# Display responses in a loop
if responses:
  st.header('Responses')
  for i, response in enumerate(responses):
    st.success(f'Response {i+1}: {response}')
