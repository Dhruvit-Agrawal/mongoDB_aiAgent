import streamlit as st
import requests

st.title("MongoDB LLM Agent UI")

st.write("Enter your natural language query to interact with the MongoDB agent.")

user_query = st.text_area("Your Query:", height=150)

if st.button("Send Query"):
    if not user_query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Sending query to agent..."):
            
        
            api_url = "http://localhost:8000/query"
            try:
                response = requests.post(api_url, json={"query": user_query})
                response.raise_for_status()
                data = response.json()
                if data.get("status") == "success":
                    st.subheader("Agent Response:")
                    st.json(data.get("response"))
                else:
                    st.error(f"Error from API: {data}")
            except requests.exceptions.RequestException as e:
                st.error(f"API request failed: {e}")
