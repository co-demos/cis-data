# from pprint import pprint, pformat
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='')
CORS(app)

@app.route("/<path:folder_path>/<string:html_filename>", methods=['GET'])
def serveHtml(folder_path, html_filename):  
  print("folder_path : ", folder_path)
  print("html_filename : ", html_filename)
  return render_template( folder_path + '/' + html_filename )

# run the application
if __name__ == "__main__":  
  app.run(debug=True, host='localhost', port=8800)