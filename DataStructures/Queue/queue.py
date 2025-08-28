from DataStructures.List import single_linked_list as lt
def enqueue(my_queue, element):
    lt.add_last(my_queue,element)
    return my_queue

def dequeue(my_queue):
    return lt.delete_element(my_queue,0)