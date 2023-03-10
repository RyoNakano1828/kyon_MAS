# Kyon breeding simulation Model

## タイトル
マルチエージェントシミュレーションによる千葉県におけるキョン捕獲効果の推定

## 概要
本研究では，マルチエージェントシミュレーションによって千葉県に生息するキョンの捕獲効果の推定を行う．1章では千葉県におけるキョンによる被害状況など現状の問題点を述べる．2章で関連研究の調査を行い，キョンに関して得られたデータをもとに，3章にてモデルのパラメータ設定を行う．4章では３つの施策シナリオを設定し，仮説の構築を行う．5章では３つの施策シナリオについての実験の結果と考察を行う．本研究の結果として，マルチエージェントシミュレーションによって，捕獲圧をパラメータとして変動させながら捕獲効果をシミュレーションすることで，キョンの頭数を横ばい，減少，駆逐するために必要な捕獲圧を推定することができた．

## キョンについて

キョンは森林に生息する小型の草食獣です。ニホンジカと生息する場所が重なり、常緑広葉樹の木の葉を好み秋にはカシ類の堅果も食べます。

樹皮や枯葉はむしろ少なく、ニホンジカよりも質のいい食物を選んでいます。また常緑亜高木のカクレノミも好み、ニホンジカが嫌う山野草のアリドオシも食べるために自然の植生への影響が危惧されています。

さらに数の増加で田畑のイネやイモ類、大豆の新芽、トマト、スイカ、イチゴなどの農作物への被害が出ています。人家の庭にも侵入して花壇の花や植木の葉を食べているのも発見されています。

伊豆大島では国が絶滅危惧種として指定し保護を進めているキンランや東京都の指定のギンランの食害がひどくなり地域の貴重な植物への影響が現れています。農作物では特産品の葉物野菜のアシタバへの被害が大きく、他にミカン、柿、キュウリや椿油用のツバキでも食害されています。

食害を防止するためには侵入防止のためには金網と上部の電気柵を複合させた形が有効でイノシシやシカ対策がキョンにも効果的です。

## 生態 
ア．食性 県内においては年間を通して木の葉を主に食し、秋にはシイ・カシ類の堅果も多く食している。嗜好種としてはアオキやカクレミノが知られている。同所的に生息しているニホンジカと比較すると、キョンは常緑広葉樹や堅果を多く、イネ科や枯葉、樹枝などは少なく採食していることがわかっており、ニホンジカよりも良質の食物を選択的に食している。  

イ．繁殖 キョンのメスは1産1子であり、早ければ生後半年程度で妊娠し、約210日の妊娠期間を経て出産する。県内における妊娠率は、0歳（6ヵ月未満）で6.3％、0歳（6ヵ月以上）で40.4％、1歳で68.2%、2歳以上で65.8％である（野生動物保護管理事務所 2020）。飼育下のキョンでは出産直後に発情・妊娠し、同一個体が1回／年を超す出産を行うことが知られている。出産は年間を通して行われているが、5～10月に出産のピークがあることが知られている（浅田 2014）。  

ウ．自然増加率 キョンの自然増加率（出産等による1年あたりの増加割合）は平成20（2008）から平成24（2012）年度の捕獲個体の分析より34%と推定されている（浅田 2014）。また、捕獲数や生息状況のモニタリングの結果から階層ベイズ法を用いて推定された結果では、中央値で18%（95％信用区間は9%～30%）と推定されている。  

エ．寿命と年齢構成 捕獲個体の分析によると、最高齢はメスで6～7歳、オスで5～6歳であった。2歳以上が最も多く、次いで1歳、0歳（6か月未満）、0歳（6ヵ月以上）の順で多かった（野生動物保護管理事務所 2020）。  

オ．行動圏 いすみ市において行った行動圏調査の結果によれば、平均の行動圏（95％カーネル法）はオスで4.0ha、メスで1.7haであった。個体により行動圏に農地周辺が含まれる割合が大きく異なることや、夜間にその割合が高まる傾向が見られること、良好な餌場があると休息場と餌場の移動を繰り返す可能性があることが明らかとなった（千葉県 2019）。 

参考

[千葉県キョン防除実施計画](https://www.pref.chiba.lg.jp/shizen/choujuu/kyon/documents/kyonkeikaku.pdf)

[第2次千葉県キョン防除実施計画](https://www.pref.chiba.lg.jp/shizen/choujuu/kyon/documents/2nd_kyon.pdf)

[害獣被害状況](https://www.pref.chiba.lg.jp/noushin/choujuu/yuugai/documents/r3matome.pdf)

## Related research

[状態空間モデルを用いた階層ベイズ推定法によるキョン（Muntiacusreevesi）の個体数推定，日本哺乳類学会 54(1)，p53-72，（2014）](https://www.jstage.jst.go.jp/article/mammalianscience/54/1/54_53/_pdf)

[鳥獣害対策におけるGISの活用（イノシシ）](https://agriknowledge.affrc.go.jp/RN/2010890751.pdf)

[生息頭数変化に及ぼす捕獲効果のシミュレーション（アライグマ）](https://agriknowledge.affrc.go.jp/RN/2010912451.pdf)

[イノシシの去勢は効果なさそう](http://cwwm.mine.utsunomiya-u.ac.jp/question/animal_qa)

[ドローンを用いた畑からの害獣の排除動作](https://www.jstage.jst.go.jp/article/jacc/63/0/63_637/_pdf/-char/ja)

## Model Summary

提案モデルで扱うエージェントは，キョンの食料，キョン，猟師の3種類である．本節では，各エージェントの概要について述べる．
猟師とキョンはランダムフォークにより各セルをランダムに1マスずつ移動する．
キョンは動き回り，キョンの食料のあるセルと同じセルに移動することで食料を食べることができる．各セルの食料は食べられると消えるが一定のスピードで再生する．
キョンは猟師と同じマスに到達すると一定の確率で捕獲される．また，年齢が高くなるほど自然死する確率も高くなる．生後 150 日以上経つメスのキョンは一定の確率で子を産んで増える．

モデルはテストであり、いくつかの Mesa の概念と機能を示しています。
  - マルチグリッド
  - 複数のエージェント タイプ (ハンター、キョン、農作物)
  - CanvasGrid に描画しながら、エージェントの形状に任意のテキスト (ハンターの狩猟数・キョンの体力・農作物被害など) を重ねる
  - 抽象的な親から振る舞い (ランダムな動き) を継承するエージェント
  - 複数のファイルで構成されるモデルの作成。
  - エージェントをスケジュールに動的に追加および削除する

- シミュレーションの粒度を決定する(広さ・頭数・ハンター数など)
- 捕獲圧の定義を行う（広さ・キョン頭数・ハンター数を元に算出する）
- 施策と仮説を立てる
    - ドローンによる個体数可視化・わなの見回りによる効率化
    - どういう地域でどれくらいの捕獲圧を確保することが重要かをシミュレーションする
- シナリオを設定する
    - 実験1：捕獲をしない場合
    - 実験2：現状の可視化・捕獲数の目標に到達するために必要な捕獲圧（ハンター数を求める）
    - 実験3：施策を講じたとき（ハンター数を増やす＋捕獲成功確率をあげる）
- パラメータ設定
    - 前提条件
        - 1ステップごとの時間：1日ごと
        - シミュレーション期間：6年間
    - フィールド
        - シミュレーション対象地域
            - 増殖抑制地域：勝浦市・富津市
            - 分布拡大防止地域：市原市
            - 注意地域：茂原市
        - 1マスの大きさ：50m×50m
        - 生息域の大きさ：森林面積（フィールドの大きさは一定 = 40マス×40マスで400ha）
            - 勝浦市：6,312 ha
            - 富津市：12,223 ha
            - 市原市：13,822 ha
            - 茂原市：1,623 ha
    - 被害状況（草で表現する）
        - 初期値（マス目の数は適当）
        - 農作物の成長スピード（ほぼ無限に増える）
    - キョン
        - キョン初期頭数（実数・地域によって異なる）
            - 勝浦市：3,888頭
            - 富津市：4,538頭
            - 市原市：2,884頭
            - 茂原市：40頭
        - キョン初期頭数（シミュレーション上・実数と森林面積から算出）
            - 勝浦市：250頭
            - 富津市：150頭
            - 市原市：83頭
            - 茂原市：10頭
        - キョンの捕獲計画数(シミュレーション上の頭数)
            - 勝浦市：1300頭(80頭)
            - 富津市：50頭(20頭)
            - 市原市：35頭(10頭)
            - 茂原市：20頭(5頭)
        - キョンの増加率（繁殖力・キョンの妊娠確率）：10～30%（34%）
        - キョンの減少率（寿命と死亡率）
        - キョンの行動範囲（あんまり気にしないが、1日に1マス動くことを考慮してフィールドの大きさを決めたい）
    - ハンター（わな）
        - ハンターの人数：勝浦猟友会50人
        - ハンターの行動範囲（あんまり気にしない）
        - 捕獲圧（広さ・キョン頭数・罠数を元に算出する）
        - 捕獲成功確率：20~30%
- 妥当性の確認
    - 現実的な数値になっていることを確かめる？
    - 何回もシミュレーションをして誤差を確認する？

## 研究背景・目的

日本，特に地方における有害鳥獣の被害は深刻であり，令和2年における国内の被害総額は約161億円である．

鳥獣被害が深刻化している要因として，鳥獣の生息域の拡大や，猟師高齢化に伴う狩猟による捕獲圧の低下，耕作放棄地の増加などがあげられる．また，鳥獣被害は，営農意欲の減退や農業従事者の農業離れの原因となることや，耕作放棄地の増加による土砂災害の誘発など，被害額として数字に現れる以上に農山漁村に深刻な影響がある．上記に加えて，千葉県では現在特定外来種「キョン」(Muntiacus reevesi)による被害が深刻化しているという問題がある．

キョンは中国南東部及び台湾に自然分布しているシカ科の哺乳類で，千葉県におけるキョンの移入源は勝浦市にあった私立観光施設（平成 13（2001）年閉園）
と考えられており，移入時期は昭和 30（1960）年代から昭和 60（1980）年代の間であると推定されている．野生生物の本来の移動能力を超えて，人為的に，意図的・非意図的に，他の地域から導入された外来種は，在来種の捕食や競合等，地域固有の生物相や生態系に対する大きな脅威となっている．現在の千葉県の状況から，早急にキョンを防除する必要がある．千葉県の掲げる防除計画について，外来生物法に基づく防除実施計画を策定し，県，市町村，農業者，関係団体，県民等が，それぞれの役割を担い，県内のキョン問題に対する共通の理解を深め，情報の共有化を図ることにより，効果的で継続的な防除を実施することを目的としている．キョンの防除に関しては，現在千葉県をはじめとする各自治体や地元の猟師による駆除活動が進められている．実態として繁殖に対する駆除が追いついておらず，対症療法的に駆除活動を促進しているのが現状である．千葉県の掲げるキョン防除計画2) において，捕獲圧を高めるという表現が用いられているが，実際にキョンの完全駆除を実現するための指標としては，定量性に欠ける部分がある．有害鳥獣における捕獲効果をシミュレーションによって計測するという先行事例はあるが，キョンに関したシミュレーションについてはまだ行われていない．

そこで本研究では，マルチエージェントシミュレーションを用いて，現状のキョンの捕獲効果を推定し，施策を講じることで，キョンを千葉県から完全に駆逐するために必要な捕獲圧の数値を定量的に算出することを目的とする．


## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    # First, we clone the Mesa repo
    $ git clone https://github.com/RyoNakano1828/kyon_MAS.git
    $ cd kyon_MAS
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8522/](http://127.0.0.1:8522/) and press Reset, then Run.

## Files

- random_walk.py:RandomWalker エージェントを定義する．このエージェントには，1 ステップに 1 つのセルをランダムに移動する動作を実装されている．キョンエージェントと 猟師エージェントの両方が RandomWalker エージェント継承する．
- agents.py：キョンエージェントと猟師エージェントとキョンの食料エージェントを定義する．各エージェントの初期化とパラーメータの設定，1 ステップごとの行動の定義を行う．
- scheduler.py：1 ステップごとに条件を満たす各エージェントの数を返す get_type_count 関数を定義する．例えば，捕獲されたキョンの数を数えるとき，捕獲した猟師に捕獲フラグを持たせてカウントすることができる．
- model.py：初期エージェント数などのパラメータを設定し，エージェントの生成を行う．指定されたステップ数を繰り返したのち，シミュレーションの結果を CSV ファイルに書き出す．
- server.py：可視化サーバーのタイトルやエージェントの可視化やグラフ生成などの設定を行う．また，サーバー起動時のポート番号を設定する．
- run.py：``mesa runserver``コマンドにて，モデル可視化サー
バーを起動する．http://127.0.0.1:8522/ にアクセスすることでローカル環境のブラウザでシミュレーションを実施できる．ブラウザは Chrome のバージョン:108.0.5359.126 を用いた．
