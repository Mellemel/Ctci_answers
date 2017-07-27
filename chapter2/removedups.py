from LinkedList import LinkedList


def linkedlist_remove_dups(ll):
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(2)
    ll.add_node(3)
    print(ll)
    ll.delete_node(2)
    print(ll)


ll = LinkedList()
linkedlist_remove_dups(ll)
