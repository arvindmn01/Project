

lis_=list(map(int,input().strip().split()))

def rank_problem(lis):
    not_in_lis=[]
    for i in range(lis[0],lis[-1]):
        if i not  in lis:
            not_in_lis.append(i)
        else:
            pass
    if len(not_in_lis)==0:
        return 'valid'
    else:
        return f'invalid and these element are not present : {not_in_lis}'

print(rank_problem(lis=lis_))