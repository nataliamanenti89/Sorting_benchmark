
def pancake_sort(arr):

    limit= len(arr) 

    mi = arr.index(max(arr[0:limit]))



    arr= arr[mi::-1] + arr[mi + 1:]



    arr= arr[limit - 1::-1] + arr[limit:]


    limit-= 1
    return arr

def main(): 
   
    arr = ["Igor Oliveira","Cecília da Mota","Dra. Antonella da Costa","Evelyn Rodrigues","Gustavo Lima","Sr. João Pedro Cavalcante","Caleb Aparecida","Larissa Freitas",]
    print(f"Lista antes de ser ordenada: {arr}") 
    arr = pancake_sort(arr) 
    print(f"Lista ordenada do pancake: {arr}")

main() 
