def solution(n, k):
    answer = 0
    k_num_system_string = ''
    while n != 0:
        k_num_system_string += str(n % k)
        n = n // k
    k_num_system_string = k_num_system_string[::-1]
    check_prime_list = [int(x) for x in k_num_system_string.split('0') if len(x) != 0]

    def is_prime(num):
        if num == 1:
            return False
        max_num = int((num + 1) ** 0.5) + 1
        for i in range(2, max_num):
            if num % i == 0:
                return False
        return True

    for number in check_prime_list:
        if is_prime(number):
            answer += 1
    return answer


if __name__ == "__main__":
    n_list = [437674, 110011]
    l_list = [3, 10]
    result_list = [3, 2]
    for n, k, result in zip(n_list, l_list, result_list):
        answer = solution(n, k)
        print(f'answer : {answer} | result {result}')
