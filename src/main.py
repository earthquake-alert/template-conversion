'''
@author: Yuto Watanabe

Copyright (c) 2020 Earthquake alert
'''
import ast
from datetime import datetime, timedelta, timezone

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/template')
def template():
    '''
    Generate a page to which the template is applied.
    '''
    title = request.args.get('ti') or 'No data.'
    areas = ast.literal_eval(request.args.get('areas') or '{"Null": ["No area."]}')
    explanation = ast.literal_eval(request.args.get('exp') or '["No data.", "No data."]')
    max_seismic_intensity = request.args.get('max_si') or 'No data.'
    epicenter = request.args.get('epi') or 'No data.'
    magnitude = request.args.get('mag') or 'No data.'
    date = request.args.get('date') or None

    if date is None:
        jst = timezone(timedelta(hours=+9), 'JST')
        now = datetime.now(jst)
    else:
        now = datetime.strptime(str(date), r'%Y%m%d%H%M%S')

    is_tsunami = False
    for element in explanation:
        if '津波' in element and 'この地震による津波の心配はありません。' not in element:
            is_tsunami = True
            break

    seismic = ''
    if max_seismic_intensity in {'0', '０'}:
        seismic = 'class-0'
    elif max_seismic_intensity in {'1', '１'}:
        seismic = 'class-1'
    elif max_seismic_intensity in {'2', '２'}:
        seismic = 'class-2'
    elif max_seismic_intensity in {'3', '３'}:
        seismic = 'class-3'
    elif max_seismic_intensity in {'4', '４'}:
        seismic = 'class-4'
    elif max_seismic_intensity in {'5弱', '５弱'}:
        seismic = 'class-5'
    elif max_seismic_intensity in {'5強', '５強'}:
        seismic = 'class-55'
    elif max_seismic_intensity in {'6弱', '６弱'}:
        seismic = 'class-6'
    elif max_seismic_intensity in {'6強', '６強'}:
        seismic = 'class-66'
    elif max_seismic_intensity in {'7', '７'}:
        seismic = 'class-7'
    else:
        seismic = 'none'

    return render_template('index.html',
                           title=title,
                           areas=areas,
                           explanation=explanation,
                           max_seismic_intensity=max_seismic_intensity,
                           epicenter=epicenter,
                           magnitude=magnitude,
                           seismic=seismic,
                           date=now.strftime('%Y年%m月%d日 %H:%M:%S'),
                           is_tsunami=is_tsunami
                           )


@app.route('/report')
def prompt_report():
    '''
    For seismic intensity flash report
    '''
    title = request.args.get('ti') or 'No data.'
    areas = ast.literal_eval(request.args.get('areas') or '{"Null": ["No area."]}')
    explanation = ast.literal_eval(request.args.get('exp') or '["No data.", "No data."]')
    max_seismic_intensity = request.args.get('max_si') or 'No data.'
    date = request.args.get('date') or None

    if date is None:
        jst = timezone(timedelta(hours=+9), 'JST')
        now = datetime.now(jst)
    else:
        now = datetime.strptime(str(date), r'%Y%m%d%H%M%S')

    is_tsunami = False
    for element in explanation:
        if '津波' in element and 'この地震による津波の心配はありません。' not in element:
            is_tsunami = True
            break

    seismic = ''
    if max_seismic_intensity in {'0', '０'}:
        seismic = 'class-0'
    elif max_seismic_intensity in {'1', '１'}:
        seismic = 'class-1'
    elif max_seismic_intensity in {'2', '２'}:
        seismic = 'class-2'
    elif max_seismic_intensity in {'3', '３'}:
        seismic = 'class-3'
    elif max_seismic_intensity in {'4', '４'}:
        seismic = 'class-4'
    elif max_seismic_intensity in {'5弱', '５弱'}:
        seismic = 'class-5'
    elif max_seismic_intensity in {'5強', '５強'}:
        seismic = 'class-55'
    elif max_seismic_intensity in {'6弱', '６弱'}:
        seismic = 'class-6'
    elif max_seismic_intensity in {'6強', '６強'}:
        seismic = 'class-66'
    elif max_seismic_intensity in {'7', '７'}:
        seismic = 'class-7'
    else:
        seismic = 'none'

    return render_template('index_report.html',
                           title=title,
                           areas=areas,
                           explanation=explanation,
                           max_seismic_intensity=max_seismic_intensity,
                           seismic=seismic,
                           date=now.strftime('%Y年%m月%d日 %H:%M:%S'),
                           is_tsunami=is_tsunami
                           )


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
