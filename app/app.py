from flask import Flask, request, abort, Response
import os

# Initialize a Flask application
app = Flask(__name__)

# Define a route for '/data' that only accepts GET requests


@app.route('/data', methods=['GET'])
def get_data():
    # Retrieve 'n' and 'm' query parameters from the URL
    file_name = request.args.get('n')  # 'n' is the name of the file
    line_number = request.args.get('m')  # 'm' is the line number

    # Check if 'n' (file name) is provided, abort with a 400 error if not
    if not file_name:
        abort(400, description="File name (n) is required")

    # Construct the file path using the provided file name
    file_path = f'/tmp/data/{file_name}.txt'

    # Check if the file exists, abort with a 404 error if not
    if not os.path.exists(file_path):
        abort(404, description="File not found")

    # If 'm' (line number) is provided
    if line_number:
        try:
            # Convert line number to an integer
            line_number = int(line_number)
            # Stream the file content and find the specified line

            def generate_lines():
                with open(file_path, 'r') as file:
                    for i, line in enumerate(file, 1):
                        if i == line_number:
                            yield line
                            return  # Stop streaming after finding the line
                        yield line

            return Response(generate_lines(), content_type='text/plain')
        except ValueError:
            # If line number cannot be converted to an integer, abort with a 400 error
            abort(400, description="Invalid line number")
    else:
        # Stream the entire file content
        def generate_file():
            with open(file_path, 'r') as file:
                for line in file:
                    yield line

        return Response(generate_file(), content_type='text/plain')


# Run the Flask application on host 0.0.0.0 and port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
