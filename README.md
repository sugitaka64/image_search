# 画像検索サンプル

## 概要

指定した画像に対して、ディレクトリの中から似た画像を探します。  
OpenCVを使います。

## 環境

* マシン/OS
  * MacBook Pro (Retina, 15-inch, Mid 2014)
  * OS X Yosemite 10.10.5
* Python
  * Python 3.5.2 :: Anaconda 4.1.1 (x86_64)
* Pythonパッケージ
  * opencv3 3.1.0（[conda](https://anaconda.org/menpo/opencv3)でインストールします。）

## ディレクトリ構成

```shell-session
hist_matching.py
feature_detection.py
images_min
 └─ ここに画像を置いてください
```

## 使い方

### ヒストグラム比較

```shell-session
$ cd /path/to/image_search
$ python hist_matching.py --target_img_path=<検索対象のファイルパス>
```
類似度の高い順（スコア降順）に結果が10件表示されます。

### 特徴点のマッチング

```shell-session
$ cd /path/to/image_search
$ python feature_detection.py --target_img_path=<検索対象のファイルパス>
```
類似度の高い順（スコア昇順）に結果が10件表示されます。

## TODO

* 検索対象のディレクトリを引数で指定できるようにする
* 表示件数を引数で指定できるようにする
* GIFファイルが読み込めないのをなんとかする

## 参考

* http://qiita.com/best_not_best/items/c9497ffb5240622ede01
