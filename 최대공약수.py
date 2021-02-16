#https://codepractice.tistory.com/65

# 최대공약수 1
def gcd(a, b):   
    if a < b:
        (a, b) = (b, a) 
    while b != 0: 
        (a, b) = (b, a % b)
    return a


# 최대공약수 2
    i = min(n, m)
    while i >= 0:
        if n % i == 0 and m % i == 0 or i == 1:
            answer.append(i)
            break
        else:
            i -= 1
            
# 최소공배수는 a*b=최대공약수*최소공배수 임을 이용하자
