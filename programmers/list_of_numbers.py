#!/usr/bin/env python3



def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


if __name__ == "__main__":
    pb1 = ['119', '94674223', '1195524421']
    pb2 = ['123', '456', '789']
    pb3 = ['12', '123', '1235' '567', '88']

    print(solution(pb1)) # return False
    print(solution(pb2)) # return True
    print(solution(pb3)) # return False
