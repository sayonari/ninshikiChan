import speech_recognition as sr
from googletrans import Translator
import codecs

#######################################
# 初期設定 -----------------------------
lang_in = 'ja'
lang_dest = 'en'





#######################################
# 以下　プログラム
#######################################

# 最初の初期化 --------------------------
translator = Translator()
r = sr.Recognizer()
mic = sr.Microphone()
cnt = 0

while True:
    # 毎回の初期化 ----------------------
    recog_text = ''

    # 音声録音 -------------------------
    with mic as source:
        print('START! [{}]'.format(cnt))
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # 音声認識 -------------------------
    try:
        recog_text = r.recognize_google(audio, language='ja-JP')
    except:
        pass

    print(recog_text)
    cnt = cnt + 1

    # 翻訳 --------------------------
    translatedText = ''
    try:
        translatedText = translator.translate(recog_text, src=lang_in, dest=lang_dest).text
    except:
        pass

    print(translatedText)

    if recog_text:
        # テキストファイルの作成 ------------------
        out_file = codecs.open('out.txt', 'w', 'utf-8')

        print(recog_text.decode('shiftjis'), file=out_file)
        print(translatedText.decode('shiftjis'), file=out_file)

        # ファイルを閉じる ----------------
        out_file.close()
