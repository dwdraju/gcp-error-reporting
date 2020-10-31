from flask import Flask, json
from google.cloud import storage

default = [{"success": "true"}]

api = Flask(__name__)

try:
  import googleclouddebugger
  googleclouddebugger.enable(
    breakpoint_enable_canary=True
  )
except ImportError:
  pass

@api.route('/storage', methods=['GET'])
def get_storage():
    bucket_name = "run-storage"
    source_file_name = "test"
    destination_blob_name = "test"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
    return json.dumps(default)

@api.route('/')
def index():
    return json.dumps(default)

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')
