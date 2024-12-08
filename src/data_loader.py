import json

def load_tracking_data():
    """Load shipment tracking data from a file or API."""
    try:
        with open('tracking_data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {
            "package_id": "123456",
            "status": "In Transit",
            "current_location": "Los Angeles, CA",
            "estimated_delivery": "2024-12-10"
        }
