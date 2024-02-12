def find_dominant_element(A):
    dom_num = len(A)//2
    print(f"Dom repeat is : {len(A)}/2 = {dom_num}")
    real_A = list(set(A))
    element_dic = {}
    for i in real_A:
        repeat_i = 0
        for j in A:
            if i == j:
                repeat_i += 1
        element_dic.update({i:repeat_i})
    for x,y in element_dic.items():
        if y >= dom_num:
            print(f"the num {x} repeats {y} times")
A = [1,2,3,4,5,3,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,4,3,2,1,1,1,3,3,3,3,5,2]
print(f"given List :{A}")
find_dominant_element(A)
