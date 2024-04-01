a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

srt_sub = r'C:\Users\prude\SynologyDrive\vscode\my_project\qt_django_tube\views\[English (auto-generated)] Object Tracking with YOLOv5 and DeepSORT in OpenCV [DownSub.com].srt'

# 리스트 3배수 제거 
def delete_3m(list_obj):    
    result = [row for i, row in enumerate(list_obj) if i % 4 != 0]
    return result

def chage_dot(list_obj):
    '''
    2,6,10 ... 으로 가는 규칙을 찾아서 
    '''
    result = []
    for i, row in enumerate(list_obj, start=3):
        if (i % 4) == 0:
            row = row.replace(',','.')
        result.append(row)
    # print(result)
    return result

with open(srt_sub, 'r') as f:
    subs = f.readlines()
    subs = chage_dot(subs)
    subs = delete_3m(subs)    
    subs = [ sub.split('\n')[0] for sub in subs ]
    
# 텍스트 파일 열기
out_path = "[English (auto-generated)] Object Tracking with YOLOv5 and DeepSORT in OpenCV [DownSub.com].srt_to.vtt"
with open(out_path.replace('[English (auto-generated)] ',''), "w") as f:
    f.write('WEBVTT\n\n')
    # 문자열 리스트를 파일에 쓰기
    for string in subs:
        f.write(string + "\n")





