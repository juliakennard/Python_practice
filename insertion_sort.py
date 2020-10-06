##  Pseudo code
    # Compare arr[1] and arr[0]
    # Move smaller number to front
    # Compare arr[2] to arr[1]
        # If arr[2] < arr[1]
            #Compare arr[2] to arr[0]
                # If arr[2] < arr[0]
                    # Move arr[2] to arr[0]
                    # Move arr[0] to arr[1]
        # If arr[2] >= arr[1] 
            # Move on
    # Compare arr[3] to arr [2]
        # If arr[3] < arr[2]
            # Compare arr[3] to arr[1]
                # If arr[3] < arr [1]
                    # Compare arr[3] to arr[]

my_array = [4,3,2,1]

def insertion_sort(some_array):
    if some_array[1] < some_array[0]:
        some_array[1] = 