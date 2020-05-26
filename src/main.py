from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/template')
def template():
    title = request.args.get('title')
    # areas = request.args.get('areas')
    # explanation = request.args.get('exp')
    # max_seismic_intensity = request.args.get('max_si')
    # epicenter = request.args.get('epi')
    # magnitude = request.args.get('mag')

    return render_template('index.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)
