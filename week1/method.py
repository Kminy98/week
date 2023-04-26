# ----------문자열 메서드----------

# count: 문자열 내에서 특정 문자가 몇개나 있는지 세는 메서드
min = "Hello! Min Young"
count = min.count('o')
print(count) # 2

# find: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드(없을경우 -1 return!!)
find_ = min.find("Min")
print(find_) # 7

# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없으면 ValueError )
try:
    index_ = min.index("Min")
    print(index_) # 7
except ValueError:
    print("없음")
# join: 특정 문자열을 기준으로 다른 문자열을 합쳐주는 메서드(sql의 join과는 다름/os.path.join())
min_join = ["Hello", "Min", "Young"]
join_ = ''.join(min_join)
print(join_) # HelloMinYoung

# upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드(대소문자를 구분하지않고 검색할 때 자주사용)
upper_ = min.upper()
print(upper_) # HELLO! MIN YOUNG

# lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드(대소문자를 구분하지않고 검색할 때 자주사용)
lower_ = min.lower()
print(lower_) # hello! min young

# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
replace_ = min.replace('Hello', '안녕')
print(replace_) # 안녕! Min Young

# split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
split_ = min.split('!')
print(split_) # ['Hello', ' Min Young']



# ----------리스트 메서드----------

# len: 리스트의 길이를 반환해주는 메서드
min = [1,2,3,4,5]
print(len(min)) # 5

# del: 리스트에서 특정 요소를 삭제하는 연산자
del min[2]
print(min) # [1, 2, 4, 5]

# append:리스트의 맨뒤에 새로운 요소를 추가
min.append(0)
print(min) # [1, 2, 4, 5, 0]

# sort: 리스트를 오름차순으로 정렬하는 메서드(reverse=True를 인자로 주면 내림차순/sorted()는 원래)
min.sort()
print(min) # [0, 1, 2, 4, 5]

# reverse: 순서를 반대로 뒤집는다
min.reverse()
print(min) # [5, 4, 2, 1, 0]

# index: 리스트에서 특정 요소의 인덱스를 반환하는 메서드
print(min.index(4)) # 1

# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
min.insert(2,2)
print(min) # [5, 4, 2, 2, 1, 0]

# remove: 리스트에서 특정 요소를 제거하는 메서드
min.remove(0)
print(min) # [5, 4, 2, 2, 1]

# pop: 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드(()안에 위치를 정하면 해당 위치 요소가 삭제)
min.pop()
print(min) # [5, 4, 2, 2]

min.pop(0)
print(min) # [4, 2, 2]

# count: 리스트에서 특정 요소의 개수를 세는 메서드
print(min.count(2)) # 2

# extend: 리스트를 확장하여 새로운 요소들을 추가하는 메서드(+= 연산자를 사용해서도 구현 할 수도 있음(좀더 일상적으로 사용함))
min.extend([6,7,8,9])
print(min) # [4, 2, 2, 6, 7, 8, 9]



# ----------딕셔너리 메서드: 키,벨류 쌍으로 저장해야할때, 시간복잡도는 상수로저장 hash?----------

# 딕셔너리 초기화
# 빈딕셔너리 만들기 - 변수={}
# 초기화할 딕셔너리만들기 - {"키":값,"키":값}
empty_dict = {}
min = {"a":1, "b":2, "c":3 }
print(min) # {'a': 1, 'b': 2, 'c': 3}

# 딕셔너리 쌍 추가: 변수["키"]=값
min["d"] = 4
print(min) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# del: 딕셔너리에서 특정 요소를 삭제
del min["a"]
print(min) # {'b': 2, 'c': 3, 'd': 4}

# 딕셔너리에서 특정 Key에 해당하는 Value 찾기 (값을 불러올때 키값이 없으면 키에러)
print(min["b"]) # 2

# keys: 딕셔너리에서 모든 Key를 리스트로 만들기
keys_ = list(min.keys())
print(keys_) # ['b', 'c', 'd']

# values: 딕셔너리에서 모든 Value를 리스트로 만들기
values_ = list(min.values())
print(values_) # [2, 3, 4]

# items: 딕셔너리의 모든 키와 값을 튜플(상수화된 리스트) 형태의 리스트로 반환
items_ = min.items()
print(items_) # dict_items([('b', 2), ('c', 3), ('d', 4)])

# clear: 딕셔너리의 모든 요소를 삭제
min.clear()
print(min) # {}

# get: 딕셔너리에서 지정한 키에 대응하는 값을 반환
# request.POST['key'] -> 키에러
# request.POST.get('key') -> 키에러가 안나고 None 반환 (추천)
min = {"a":1, "b":2, "c":3 }
get_ = min.get('b')
print(get_) # 2

get_ = min.get('d')
print(get_) # None

get_ = min.get('d','없음')
print(get_) # 없음

# in: 해당키가 딕셔너리 안에 있는지 확인(모든 순회가능한 것에 사용가능)
print("c" in min) # True
print("d" in min) # False