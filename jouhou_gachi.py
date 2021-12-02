# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:09:39 2021

@author: ItoKaito
"""

import streamlit as sｔ

st.title('ストレスフルアプリ')

st.header('あなたは今どんな気分ですか？あなたの気分に合わせたアドバイスや手立てを提案します！今日はちょっといい日になるかも|дﾟ)')



text = st.text_input('あなたの名前を教えてください')
'あなた',text,'っていうのね！'


option = st.selectbox( 'あなたの今の気分を教えてね',
('Not select','めちゃくちゃ元気盛り上がりたい', '彼氏・彼女に振られた/しんどい気分', '家族が恋しい',
 'これから寝ます'))


if option==('めちゃくちゃ元気盛り上がりたい'):
    
    txt = st.text_area('盛り上がりたい理由を教えて')
    
    
    st.header('そんな時はこの歌を聴こう！')
    
    st.subheader('『雨上がりの歌』')
    
    
    st.write('見てよ昨日の雨もほら')
    st.write('道路も乾いてココロオドル')
    st.write('顔を上げれば草も木も')
    st.write('君も笑う踊りだそうよ')
    
    st.write('コオロギ　トッポギ　六本木')
    st.write('コオロギ　トッポギ　六本木')
    st.write('コオロギ　トッポギ　六本木')
    st.write('official　ひげ総理　sorry')
    
    st.write('立ち上がって　前を向いて')
    st.write('両手叩いて　今日も元気に！')
    
    
    audio_file = open('morimori.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    
elif option==('彼氏・彼女に振られた/しんどい気分'):
    
   
    
    genre = st.radio(text+"はどういうタイプ？",
     ('Not select','強がっているのを友達に見せたくない', '「どうせ私なんか」「僕なんか」という言葉を使ってしまう',))
    
    if genre == '強がっているのを友達に見せたくない':
        txt = st.text_area('どんなことがしんどいのか教えてよ！')
        
         
    elif genre == '「どうせ私なんか」「僕なんか」という言葉を使ってしまう':
        st.write('生きているだけで偉いんだよ')
    
    st.header('そんな時はこの歌を聴こう！')
    
    st.subheader('『YUZAME』')
    
    
    st.write('風呂を出たら…')
    st.write('通知画面に…')
    st.write('風呂を出た　濡れた体は')
    st.write('通知のせいで　濡れたままだ')
    st.write('僕のことは　君はもうすでに')
    st.write('好きじゃないのか　そっかそっか')
    st.write('冷めてゆく　濡れた身体')
    
    st.write('（恋は湯冷め）')
    
    st.write('恋冷め　湯冷め')
    st.write('想いは流れ')
    st.write('熱とともに消えてゆく')
    st.write('身体とともに消えてゆく')
    st.write('君の想いは　消えてゆく')
    st.write('恋覚め　湯冷め')
    st.write('想いは流れて')
    st.write('熱は身体から消えてゆく')
    st.write('想いはきっと冷めてゆく')
    
    st.write('これは湯冷め')
    
    audio_file = open('yuzame.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    
          
elif option==('家族が恋しい'):
    
    genre = st.radio(text+"はどうして家族が恋しいの？",
    ('Not select','なかなか生活に慣れない','知り合いができない','家族と離れて大丈夫かな','友達がいなくて孤独'
     ,'新生活がうまくいかなくて不安'))
    st.write('どんなことが自分のストレスになっているのか知ることは大切だよ！')
    txt = st.text_area('家族に会ったら何したい？')
    genre = st.radio(text+"はどうやってホームシックな気持ちを乗り越える？",
                     ('Not select','ストレスに対する考え方を変えてみる','がまんして時間が解決してくれるのを待ってみる'
                      ,'家族や友達にLINE・電話する','我慢しないで泣く','テレビや本を読む'
                      ,'今の場所で友達を作る','仕事や趣味に没頭する','目的を見つめなおす'
                      ,'帰省しちゃう','実家暮らしに戻る'))
    if genre == 'ストレスに対する考え方を変えてみる':
        st.write('「私にはこんなことできないよ」と思うか、「次はこうすればよくなる」と思うかで違いますよ？')
    
    elif genre =='がまんして時間が解決してくれるのを待ってみる':
        st.write('自分の本当の限界まで周囲に甘えず待ってみるのもいい選択ですね')
    
    elif genre =='家族や友達にLINE・電話する':
        st.write('親しい人との会話って落ち着くし幸福感が溢れますよね！')
    
    elif genre =='我慢しないで泣く':
        st.write('泣けそうっだったら泣てしまうとすっきりしてストレス解消につながるというのは根拠のあるストレス解消法ですよ')
        
    elif genre =='テレビや本を読む':
        st.write('一人でいるといろいろ考えちゃうもんね')
        
    elif genre =='今の場所で友達を作る':
        st.write('友達ができると安心するし、案外同じ悩みを抱えているのかもしれないよ')
        
    elif genre =='仕事や趣味に没頭する':
        st.write('仕事や趣味に没頭して充実した生活を送れば悩んでる暇なんてないよね'
                 ,'もしかしたらその仲間と仲良くなれて一石二鳥かも！？')
    
    elif genre =='目的を見つめなおす':
        st.write('目的を達成すれためには困難はつきものです。何をなすために自分はここにいるのかを見つめなおすいい機会ではないでしょうか')
        
    elif genre =='帰省しちゃう':
        st.write('適度に帰省しちゃえば問題ないよね！')
        
    elif genre == '実家暮らしに戻る':
        st.write('どうしても無理というなら逃げることだって一つの勇気がある選択ですよね')
        
        
        
        
        
    st.caption('ホームシックの原因は一言でいえば「人生経験のなさ」だといえます。')
    st.caption('なぜなら一人で行動する人生経験が足りていないからです。')
    st.caption('何かを成し遂げたという経験は一生ものになるはず！')
    st.caption('だから家族が恋しくてホームシックを感じたならそれはきっと成長の起爆剤になりえるチャンスです！')
    st.caption('前向きに進んでみてはいかがですか？')
    
elif option==('これから寝ます'):
    
    st.write('快眠の方法を教えてあげるよ！')
    st.write(text+'はお風呂は好き？快眠のためには就寝前に38℃～40℃位のお湯で20～30分ほどゆっくり入浴するといいんだよ！')
    st.write('他にはホットドリンクを飲む方法もあるよ！カモミールティーやホットミルクは快眠につながるといわれているから試してみてね！')
    st.write('じゃあ、おやすみ')
    
    st.header('あ、待って！寝る前にこの歌を聴こう！')
    
    
    st.subheader('『Good night baby』')
    
    st.write('静かにおねんね　よい子だよい子')
    st.write('羊を数えて　さぁ　夢の中')
    
    st.write('（羊が１匹、羊が２匹、羊が3匹、羊が4匹、羊が5匹…）')
    
    st.write('静かにおねんね　よい子だよい子')
    st.write('羊を数えて　さぁ　夢の中')
    
    st.write('静かにおねんね　今日もおつかれ')
    st.write('明日もいい日になるよ！きっとさ')
   
    
    audio_file = open('good_night.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')