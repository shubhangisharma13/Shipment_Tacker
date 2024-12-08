from flask import Flask, request, jsonify
from src.model import ShipmentTracker
from src.data_loader import load_tracking_data
from src.utils import setup_logging, log_request

app = Flask(__name__)

# Setup logging
setup_logging()

# Initialize the LLM
shipment_tracker = ShipmentTracker(api_key="your_openai_api_key_here")

@app.route('/track-shipment', methods=['POST'])
def track_shipment():
    """
    API endpoint to track the shipment.
    Request format: { "query": "Where is my shipment?" }
    """
    try:
        log_request(request)
        
        data = request.get_json()
        user_query = data.get('query', 'Where is my shipment?')
        
        # Load tracking data
        tracking_data = load_tracking_data()
        
        # Get AI response
        response = shipment_tracker.generate_tracking_response(user_query, tracking_data)
        
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
