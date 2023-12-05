from apps.model_setting.models import TestData


# 데이터 입력
def inputData(name, age):
    data = TestData(name=name, age=age)
    data.save()
    print(f'{name}, {age} 저장완료')

# 모든 데이터 조회
def all():
    datas = TestData.objects.all()
    for row in datas:
        print(row.pk, row.name, row.age)
    print('모든 데이터 조회')
        
# 이름으로 데이터 조회
def search(name):
    datas = TestData.objects.filter(name__contains = name)
    for row in datas:
        print(row.pk, row.name, row.age)
    
# 데이터 삭제
def delete_list(*args):
    TestData.objects.filter(pk__contains=[14, 15]).delete()
    


if __name__=='__main__':
    search('kim')
    print('-'*30)
    delete_list(11,13)
    search('kim')