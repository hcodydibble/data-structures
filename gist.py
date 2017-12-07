def add_linked_lists(linked1, linked2):
    from linked_list import LinkedList
    curr1 = linked1.head
    curr2 = linked2.head
    add1 = []
    add2 = []
    list3 = []
    while curr1:
        add1.append(curr1.data)
        curr1 = curr1.nxt
        if curr1 is None:
            break
    while curr2:
        add2.append(curr2.data)
        curr2 = curr2.nxt
        if curr2 is None:
            break
    strung1 = ''
    strung2 = ''
    add1 = add1[::-1]
    add2 = add2[::-1]
    for item in add1:
        strung1 += str(item)
    for item in add2:
        strung2 += str(item)
    new_list = int(strung1) + int(strung2)
    new_list = str(new_list)
    for item in new_list:
        list3.append(item)
    import pdb; pdb.set_trace()
    list3 = LinkedList(new_list)
    print(linked1.display())
    print(linked2.display())
    return list3.display()
