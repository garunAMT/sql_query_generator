import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Now you can access your API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.0-pro")

def main():
    st.title('SQL Query Generator')
    st.write('I can generate SQL queries for you')
    st.write('With explanation as well!!!')

    text_input = st.text_area('Enter the query below in plain english')
    
    
    submit = st.button('Generate SQL Query')
    if submit:
        with st.spinner('Generating SQL Query...'):
            template="""
                Create a SQL query using the below text:
                
                
                    {text_input}
                
                I just want a SQL query.
            """
            formatted_template = template.format(text_input=text_input)
            # st.write(formatted_template)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
            # st.write(sql_query)
            
            expected_output="""
                What would be the expected response of the SQL query snippet
                
                    {sql_query}
                
                Provide sample tabular Response with no explanation
            """
            
            expected_output_template = expected_output.format(sql_query=sql_query)
            e_output= model.generate_content(expected_output_template)
            e_output = e_output.text
            # st.write(e_output)

            explanation="""
                Explain the below SQL query
                
                    {sql_query}
                
                Please provide the simplest of explanation
            """
            explanation_format = explanation.format(sql_query=sql_query)
            explanation_response = model.generate_content(explanation_format)
            explanation_response = explanation_response.text
            # st.write(explanation_response)
        
            with st.container():
                st.success('SQL Query generated successfully! 🎉 Here is your query below')
                st.code(sql_query, language='sql')
                st.success('Expected Output of this SQL Query will be: ')
                st.markdown(e_output)
                st.success('Explanation of the SQL Query: ')
                st.markdown(explanation_response)
main()
