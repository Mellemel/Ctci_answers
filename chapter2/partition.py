from LinkedList import LinkedList

def partition(ll : LinkedList, num : int):
    runner = ll.head
    less_than = []
    greater_than = []
    while runner != None:
        if runner.data < num:
            less_than.append(runner)
        else:
            greater_than.append(runner)
        runner = runner.next
    ll.head = less_than[0]
    runner = None
    all_nodes = less_than + greater_than
    for node in all_nodes:
        if runner == None:
            runner = ll.head
            continue
        runner.next = node
        runner = runner.next

ll = LinkedList()
max_value = 100
ll.generate(10, 0, max_value)
print(ll)
partition(ll, max_value / 2)
print(ll)
