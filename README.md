# 프로젝트 구조
```
root
├─ apps
│  ├─ model_setting (장고앱에서 마이그레이션 지원)
│  │  └─ models.py
├─ db.sqlite3 (장고에서 생성한 DB)
├─ main.py (스타팅 포인트)
├─ manage.py (장고 명령어 관련 코드)
├─ README.md 
├─ rsc (이미지 등 리소스 관리 디렉토리)
│  ├─ assets
│  │  └─ **.png
│  └─ ui.py (ui파일에서 py파일로 변환)
├─ settings.py (장고 세팅)
├─ viewManagers 
   ├─ mainWindowManager.py (pyside6 슬롯함수 작성)
   └─ orm.py (장고 orm 컨트롤 코드)
```

# ui파일 => 파이썬 파일로 변환
untitled.ui 파일 위치에서 명령어 실행
pyside6-uic untitled.ui -o untitled_ui.py

# 0. 모델 작성
Path: root/apps/model_setting/models.py

# 1. 모델 마이그레이션 준비 
python manage.py makemigrations model_setting

# 2. 모델 마이그레이트
python manage.py migrate

***
#### Using Pyinstaller
python manage.py deploy

