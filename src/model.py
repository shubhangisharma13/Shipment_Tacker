import openai
import os

class ShipmentTracker:
    def __init__(self, api_key):
        """Initialize the LLM with the API key."""
        self.api_key = api_key
        openai.api_key = api_key

    def generate_tracking_response(self, query, tracking_data):
        """
        Generate a response to the user's query using an LLM.
        Args:
            query (str): The user's question, e.g., "Where is my shipment?"
            tracking_data (dict): Shipment details like location, status, ETA, etc.
        Returns:
            str: AI-generated response.
        """
        prompt = f"""
        You are an AI assistant for a shipment tracking company.
        The following is the tracking information for the user's package:
        {tracking_data}
        
        User's query: "{query}"
        
        Provide a clear and helpful response to the user's query.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"Error generating response: {e}"
