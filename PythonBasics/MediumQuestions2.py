# Retrieve last n numbers from a List
def retrieve_last_elements(lst,n):
    if n<=0:
        return []
    return lst[-n:]
print(retrieve_last_elements([1,2,3,4,5],2))

