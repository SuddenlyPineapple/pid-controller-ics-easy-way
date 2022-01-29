from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from multiprocessing import Process
from PIDController import PIDController


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

pid_logic = PIDController()
task_set = []

@app.route('/')
@cross_origin()
def health_check():  # put application's code here
    return jsonify({"message": "Healthy"}), 200, {"Content-Type": "application/json"}

@app.route('/state')
@cross_origin()
def check_status():
    if task_set==[] or (task_set and task_set[0].is_alive()==False):
        return jsonify({"message": "Not busy!"}), 200, {"Content-Type": "application/json"}
    else:
        return jsonify({"message": "Machine currently busy!"}), 409, {"Content-Type": "application/json"}

@app.route('/set-params', methods=['POST'])
@cross_origin()
def set_params():
    pid_logic.set_data(
     sample_time=request.args.get('sample_time',0.05),
     differential_time=request.args.get('differential_time',0.15),
     integration_time=request.args.get('integration_time',0.25),
     gain=request.args.get('gain',0.1),
     k_e=request.args.get('k_e',0.2),
     k_ce=request.args.get('k_ce',0.05),
     k_u=request.args.get('k_u',0.1),
     h_z=request.args.get('h_z',8),
     A=request.args.get('A',2.5),
     B=request.args.get('B',0.25),
     h_max=request.args.get('h_max',10),
     u_max=request.args.get('u_max',10),
     u_min=request.args.get('u_min',-10),
     Q_d_max=request.args.get('Q_d_max',1),
    )
    return jsonify({"message": "Parameters changed successfully!"}), 201, {"Content-Type": "application/json"}

@app.route('/generate-pid', methods=['POST'])
def generate_pid():
    if task_set==[] or (task_set and task_set[0].is_alive()==False):
        task_set.clear()
        heavy_process = Process(  # Create a daemonic process with heavy "my_func"
            target=pid_logic.classic_pid_chart,
            daemon=True
        )
        heavy_process.start()
        task_set.append(heavy_process)
        return jsonify({"message": "Task dispatched successfully!"}), 201, {"Content-Type": "application/json"}
    else:
        return jsonify({"message": "Machine currently busy!"}), 409, {"Content-Type": "application/json"}


@app.route('/generate-fuzzy', methods=['POST'])
def generate_fuzzy():
    if task_set==[] or (task_set and task_set[0].is_alive()==False):
        task_set.clear()
        heavy_process = Process(  # Create a daemonic process with heavy "my_func"
            target=pid_logic.fuzzy_chart,
            daemon=True
        )
        heavy_process.start()
        task_set.append(heavy_process)
        return jsonify({"message": "Task dispatched successfully!"}), 201, {"Content-Type": "application/json"}
    else:
        return jsonify({"message": "Machine currently busy!"}), 409, {"Content-Type": "application/json"}

@app.route('/generate-comparison', methods=['POST'])
def generate_comparison():
    if task_set==[] or (task_set and task_set[0].is_alive()==False):
        task_set.clear()
        heavy_process = Process(  # Create a daemonic process with heavy "my_func"
            target=pid_logic.comparison_chart,
            daemon=True
        )
        heavy_process.start()
        task_set.append(heavy_process)
        return jsonify({"message": "Task dispatched successfully!"}), 201, {"Content-Type": "application/json"}
    else:
        return jsonify({"message": "Machine currently busy!"}), 409, {"Content-Type": "application/json"}

@app.route('/get-pid-chart')
def get_pid_chart():
    return send_from_directory('static', 'plot.png')

@app.route('/get-fuzzy-chart')
def get_fuzzy_chart():
    return send_from_directory('static', 'fuzzy_chart.png')

@app.route('/get-pid-and-fuzzy-chart')
def get_pid_and_fuzzy_chart():
    return send_from_directory('static', 'comparison_chart.png')



if __name__ == '__main__':
    app.run(debug=True)