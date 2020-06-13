'''
@author: Yuto Watanabe

Copyright (c) 2020 Earthquake alert
'''
import flask

app = flask.Flask(__name__)


def post(client):
    return client.get("/report?ti=震度速報&areas={'震度４': ['松島市'],'震度３':['一関市', '仙台宮城野区', '若林区', '仙台泉区', '石巻市',\
'白石市', '名取市', '角田市', '岩沼市', '登米市']}&exp=['１２日２０時３０分ころ、地震による強い揺れを感じました。震度３以上が観測された地域をお知らせします。', '今後の情報に注意してください。']\
&max_si=4")


def test_flask():
    app.config['TESTING'] = True

    with app.test_client() as client:
        post(client)
        assert flask.request.args['ti'] == '震度速報'
        assert flask.request.args['areas'] == "{'震度４': ['松島市'],'震度３':['一関市', '仙台宮城野区', '若林区', '仙台泉区', '石巻市',\
'白石市', '名取市', '角田市', '岩沼市', '登米市']}"
        assert flask.request.args['exp'] == "['１２日２０時３０分ころ、地震による強い揺れを感じました。震度３以上が観測された地域をお知らせします。', '今後の情報に注意してください。']"
        assert flask.request.args['max_si'] == '4'
