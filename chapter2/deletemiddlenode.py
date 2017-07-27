from LinkedList import LinkedList

def delete_middle_node(ll : LinkedList):
    num_of_nodes = len(ll)
    runner = ll.head
    for i in range(num_of_nodes//2 - 2):
        runner = runner.next
    runner_up = runner.next.next
    print(runner.next.data)
    runner.next = runner_up

ll = LinkedList()
ll.generate(6, 0, 100)
print(ll)
delete_middle_node(ll)
print(ll)