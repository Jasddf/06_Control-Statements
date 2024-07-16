# string = '매개변수를 입력하면, 입력한 매개변수가 화면에 출력됩니다.'
# print(string)
# len(string)
#
# # var = [1,2,3,4,5]
# # b = sum(var)
# # print(b)
#
# def 안녕하세요():
#     print('안녕하세요. 만나서 반갑습니다.')

# 두 수를 더하는 함수
def add_numbers(a,b):
    result = a + b
    print(result)
    return result

c = add_numbers(3,5)
d = add_numbers(5,11)

# 함수 호출 및 반환값 사용
sum_result = add_numbers(5,3)
print('합계 : ', sum_result)