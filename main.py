import os, json, time
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Define a dataset and table in BigQuery
DATASET_ID = 'your_dataset_id'
TABLE_ID = 'your_table_id'

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    """Example Hello World route."""
    return f"Hello World!!!!!!"


@app.route("/event_looks", methods=['GET', 'POST', 'PUT', 'DELETE'])
def event_looks():
    # Check the request method and handle accordingly
    if request.method == 'POST':
        payload = request.get_json()
        if not payload:
            return make_response(jsonify({"error": "Invalid JSON"}), 400)

        print("Received POST request")
        print(payload)

        # Assuming you want to insert the payload into BigQuery
        table_ref = client.dataset(DATASET_ID).table(TABLE_ID)
        rows_to_insert = [payload]  # Example of how to structure rows

        errors = client.insert_rows_json(table_ref, rows_to_insert)  # Insert data
        if errors:
            return jsonify({"status": "error", "errors": errors}), 500
        return jsonify({"status": "success", "message": "Data inserted"}), 201

    elif request.method == 'GET':
        print("Received GET request")
        
        # Fetch records from BigQuery (example query)
        query = f"SELECT * FROM `{DATASET_ID}.{TABLE_ID}` LIMIT 10"
        query_job = client.query(query)

        rows = [dict(row) for row in query_job]
        return jsonify({"status": "success", "data": rows}), 200

    elif request.method == 'PUT':
        payload = request.get_json()
        if not payload or 'id' not in payload:
            return make_response(jsonify({"error": "Invalid JSON or missing ID"}), 400)

        print("Received PUT request")
        print(payload)

        # Here you can implement the logic to update an existing record
        # Example: Update record based on payload['id']

        return jsonify({"status": "success", "message": "Data updated"}), 200

    elif request.method == 'DELETE':
        payload = request.get_json()
        if not payload or 'id' not in payload:
            return make_response(jsonify({"error": "Invalid JSON or missing ID"}), 400)

        print("Received DELETE request")
        print(payload)

        # Here you can implement the logic to delete a record based on payload['id']
        # Example: Delete record logic

        return jsonify({"status": "success", "message": "Data deleted"}), 200

    else:
        return make_response(jsonify({"error": "Method not allowed"}), 405)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
