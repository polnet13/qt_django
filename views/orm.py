from apps.model_setting.models import TestData
print('orm 모듈')

# 데이터 입력
def inputData(name, age):
    try:
        data = TestData(name=name, age=age)
        data.save()
        print(f'{name}, {age} 저장완료')
    except:
        print('views.orm.inputdata 오류 발생')
    

# 모든 데이터 조회
def all():
    return TestData.objects.all()
        
# 이름으로 데이터 조회
def search_name(name):
    datas = TestData.objects.filter(name__contains = name)
    for row in datas:
        print(row.pk, row.name, row.age)
    
# 전체 데이터 삭제
def delete_all():
    TestData.objects.all().delete()

    
if __name__=='__main__':
    search_name('kim')
    print('-'*30)
    search_name('kim')