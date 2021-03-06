# 猫・犬推定アプリ
## 概要
web上でアップロードされた画像に対して、猫か犬かを推定するアプリです。
## バージョン
- Python：3.6.9
- django : 3.1.3
- heroku : 7.47.0 win32-x64 node-v12.16.2

## 動作画面
![識別画面](https://raw.githubusercontent.com/wiki/Akiyoshi999/CatdogClassifiy/images/VID_20201125_214227.gif)

## 工夫した点
- 推定モデルにVGG16の転移学習したものを利用して学習精度を高めました
- ローカル環境でデータを取得、モデルの学習をすると容量が圧迫されるのと、モデルの学習に時間がかかるため「google colaboratory」を利用して学習しました。
- 当初はtensorflow==2以降のものを利用していたが、Herokuにデプロイすると500MB以上（無料だと500MB以内しかデプロイできない）になり、アップロードできなかった。なのでTensorFlowのバージョンを下げて容量を落とし、再度デプロイしました。

## 課題点・次回挑戦したいことなど
- 識別するまでの時間がかかってしまうので、次回は処理速度が速い処理を実装したい。
- 画像生成するGANや音声認識などを実装してみたい。

## 参照
- [djangoの公式ドキュメント](https://docs.djangoproject.com/ja/3.1/)
- [DjangoアプリをHerokuにデプロイする方法](https://qiita.com/frosty/items/66f5dff8fc723387108c)
- [【Keras】転移学習とファインチューニング【犬猫判別4】](https://ymgsapo.com/2019/03/14/extend-model-and-fine-tuning/)
- [【徹底的に解説！】Djangoの基礎をマスターして、3つのアプリを作ろう！](https://www.udemy.com/course/django-3app/)
- [Google ColaboratoryをGoogle DriveにマウントしてPythonを実行する。](https://qiita.com/asakuraTsukazaki/items/e7eb1f0c43be1e0231c6)
- [Django DEBUG=Falseにすると500エラーが起きた](https://ktmemo.herokuapp.com/post/2/)
