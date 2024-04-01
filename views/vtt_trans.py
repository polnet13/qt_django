
from googletrans import Translator
import datetime
import os 

def translate_to_ko(english_word_list):
    '''
    내부적으로 사용하는 함수로 
    영어문장 리스트를 입력 받아
    번역본 리스트를 출력함
    '''
    translator = Translator()
    translations = translator.translate(english_word_list, dest='ko')
    result = [ translation.text for translation in translations ]
    return result

def translate_subtitle(file_path):
    '''
    자막 파일 경로를 입력받아서
    translate_to_ko()매서드로 번역 후 
    원래 파일 경로에 .ko.vtt 를 붙여 출력함

    '''
    with open(file_path, "r") as f:
        a = f.readlines()

        start_list = a[:3]
        content_list = a[3:]
        start_list = [ row.split('\n')[0] for row in start_list ]
        english_list = [ row.split('\n')[0] for row in content_list ]
        # 번역
        print('번역중....')
        ko_list = translate_to_ko(english_list)
        results = start_list+ko_list
    # 번역본 파일 생성
    with open(rf"{file_path}.ko.vtt", "w", encoding="utf-8") as f:
      for line in results:
        f.write(line + "\n")    


if __name__ == "__main__":
    start = datetime.datetime.now()

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('실행\n\n')

    # 자막리스트 구하기
    # 자막이 있는 폴더
    try:  # pc용 경로
        s_path = r'C:\Users\prude\OneDrive\바탕 화면\유튜브 영상'
        # 폴더내에 파일, 폴더명 모두 확보
        file_lists = os.listdir(s_path)
        print('pc 경로 진입')
    except:  # 노트북 경로
        s_path = r'C:\Users\prudent13\SynologyDrive\vscode\my_project\vvt_번역\tube'
        # 폴더내에 파일, 폴더명 모두 확보
        file_lists = os.listdir(s_path)
        print('노트북 경로 진입')
        
    # translated_subtitles = translate_subtitle(file_path)
        
    # 폴더 경로와 파일 경로 결합
    fullname_file_list = [ os.path.join(s_path, file_list) for file_list in file_lists]
    only_subtitle_files = []
    for file in fullname_file_list:
        if os.path.isfile(file):
            name, ex = os.path.splitext(file)
            print(f'name: {name.split('\\')[-1]}, \nex: {ex}')
            # file에 해당하고 확장자가 .vtt 이면서 name에 ko가 없어야 함
            if file and ex == '.vtt' and '.ko' not in name.split('\\')[-1]:
                only_subtitle_files.append(file)
        else:
            print(f'파일이 아님: {file}')
    print('영어 자막 파일만 남김')
    print(only_subtitle_files)
    # 자막파일에 .ko.vtt 붙은 자막은 제외한 자막 리스트


    # 자막파일 순회하며 자막리스트 번역하기
    import time
    for row in only_subtitle_files:
        print(f'\n작업 시작: {row} ')
        translate_subtitle(row)
        print(f'작업 끝: {row}')
        time.sleep(4)
    print('전체 작업 종료')    

    # 차단을 방지 하기 위해 작업 후 20초 쉬기
    print('\n\n'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    end = datetime.datetime.now()
    print(end-start)