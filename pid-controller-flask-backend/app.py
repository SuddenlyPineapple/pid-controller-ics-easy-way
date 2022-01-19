from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def health_check():  # put application's code here
    return 'Healthy!'


@app.route('/get-pid-chart')
def pid_chart():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    print(user)
    return user


if __name__ == '__main__':
    app.run()
