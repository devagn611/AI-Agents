import requests
import streamlit as st

def get_gemini_response(prompt):
    url = "http://localhost:8000/gemini/invoke"
    headers = {"Content-Type": "application/json"}
    data = {"input": prompt}
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error in API call"}