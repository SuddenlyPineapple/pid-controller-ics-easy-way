from flask import Flask, request, send_from_directory
from multiprocessing import Process
from PIDController import PIDController


app = Flask(__name__)

pid_logic = PIDController()

@app.route('/')
def health_check():  # put application's code here
    return 'Healthy!'


@app.route('/set-params', methods=['POST'])
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
    return "OK", 201, {"Content-Type": "application/text"}

@app.route('/generate-pid', methods=['POST'])
def generate_pid():
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=pid_logic.classic_pid_chart,
        daemon=True
    )
    heavy_process.start()
    return "OK", 201, {"Content-Type": "application/text"}

@app.route('/generate-fuzzy', methods=['POST'])
def generate_fuzzy():
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=pid_logic.fuzzy_chart,
        daemon=True
    )
    heavy_process.start()
    return "OK", 201, {"Content-Type": "application/text"}

@app.route('/generate-comparison', methods=['POST'])
def generate_comparison():
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=pid_logic.comparison_chart,
        daemon=True
    )
    heavy_process.start()
    return "OK", 201, {"Content-Type": "application/text"}

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