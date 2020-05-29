# template-conversion

![python](https://img.shields.io/github/pipenv/locked/python-version/earthquake-alert/template-conversion?style=flat-square)
![license](https://img.shields.io/github/license/earthquake-alert/template-conversion?style=flat-square)

🇯🇵| [🇺🇸](documents/README_en.md)

![image](assets/demo_1.png)

## tl;dr

- URLクエリパラメータに入力した内容にテンプレートを適用させます。
- Seleniumなどで画面キャプチャをすると簡単に画像として保存できます。

## 💻使い方

1. 依存関係のインストール
   - python3、およびpipがインストールされていることが前提です。

    ```bash
    # pipを使用してpipenvをインストールする
    pip install pipenv

    # case.1 pipenvの仮想環境上にインストールする & 仮想環境を立ち上げる
    pipenv install
    pipenv shell

    # システム上にインストールする（pipでライブラリを操作可）
    pipenv install --system --deploy
    ```

2. 起動する

    ```bash
    python src/main.py
    ```

デフォルトURL: `http://localhost:5000/template`

### 📒クエリパラメータの説明

例: `http://localhost:5000/template?ti=震源・震度に関する情報&areas={'震度４': ['松島市'],'震度３':['一関市', '仙台宮城野区', '若林区', '仙台泉区', '石巻市', '白石市', '名取市', '角田市', '岩沼市', '登米市']}&exp=['１８日１２時００分ころ、地震がありました。', 'この地震による津波の心配はありません。']&max_si=4&epi=宮城県沖&mag=5.2`

![image](assets/demo_2.png)

- `ti`
  - タイトル。緊急地震速報や地震速報など。
- `areas`
  - 地震の発生エリア。画像では緑のところ。
  - `Dict[str, List[str]]`で記述。

    ```json
    {
        "震度~": [
            "エリア1",
            "エリア2",
            "エリア3",
            ...
        ],
        "震度~": [
            "エリア4",
            "エリア5",
            "エリア6",
            "エリア7",
            "エリア8",
            ...
        ]
        ...
    }
    ```

- `exp`
  - 説明。2つ以上必要です。
  - 最初の１つ目は右のトップに表示されます。
  - 2個目以上は左側に要素別にBoxで表示されます。

    ```json
    [
        "説明",
        "説明2",
        ...
    ]
    ```

- `max_si`
  - 最大震度
  - `0, 1, 2, 3, 4, 5弱, 5強, 6弱, 6強, 7`が適用されます。（数字の全角可）
  - 最大震度により背景色が変わりますが、正しくない震度が入力された場合は以下のようになります。
    ![image](assets/demo_3.png)
- `epi`
  - 震源地
- `mag`
  - マグニチュード

### 🎨震度色

| 震度  |                                    色                                     |
| :---: | :-----------------------------------------------------------------------: |
|   0   | ![#e1e2e3](https://via.placeholder.com/15/e1e2e3/000000?text=+) `#e1e2e3` |
|   1   | ![#56a0d1](https://via.placeholder.com/15/56a0d1/000000?text=+) `#56a0d1` |
|   2   | ![#204eba](https://via.placeholder.com/15/204eba/000000?text=+) `#204eba` |
|   3   | ![#d6e673](https://via.placeholder.com/15/d6e673/000000?text=+) `#d6e673` |
|   4   | ![#dbde28](https://via.placeholder.com/15/dbde28/000000?text=+) `#dbde28` |
|  5-   | ![#eba22d](https://via.placeholder.com/15/eba22d/000000?text=+) `#eba22d` |
|  5+   | ![#eba22d](https://via.placeholder.com/15/eba22d/000000?text=+) `#eba22d` |
|  6-   | ![#e62929](https://via.placeholder.com/15/e62929/000000?text=+) `#e62929` |
|  6+   | ![#e62929](https://via.placeholder.com/15/e62929/000000?text=+) `#e62929` |
|   7   | ![#a81d5b](https://via.placeholder.com/15/a81d5b/000000?text=+) `#a81d5b` |
| None  | ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000` |

### ⚖ライセンス

[MIT ライセンス](LICENSE)上で公開しています。
