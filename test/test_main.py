'''
@author: Yuto Watanabe

Copyright (c) 2020 Earthquake alert
'''
import flask

app = flask.Flask(__name__)


def post(client):
    return client.get("/template?ti=震源・震度に関する情報&areas={'震度４': ['松島市'],'震度３':['一関市', '仙台宮城野区', '若林区', '仙台泉区', '石巻市',\
'白石市', '名取市', '角田市', '岩沼市', '登米市']}&exp=['１８日１２時００分ころ、地震がありました。', 'この地震による津波の心配はありません。']&max_si=4&epi=宮城県沖&mag=5.2")


def test_flask():
    app.config['TESTING'] = True

    with app.test_client() as client:
        post(client)
        assert flask.request.args['ti'] == '震源・震度に関する情報'
        assert flask.request.args['areas'] == "{'震度４': ['松島市'],'震度３':['一関市', '仙台宮城野区', '若林区', '仙台泉区', '石巻市',\
'白石市', '名取市', '角田市', '岩沼市', '登米市']}"
        assert flask.request.args['exp'] == "['１８日１２時００分ころ、地震がありました。', 'この地震による津波の心配はありません。']"
        assert flask.request.args['max_si'] == '4'
        assert flask.request.args['epi'] == '宮城県沖'
        assert flask.request.args['mag'] == '5.2'
