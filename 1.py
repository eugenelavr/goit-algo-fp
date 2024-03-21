class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort_list(head):
    if not head or not head.next:
        return head

    # Розбиття списку на дві половини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивне сортування обох половин
    left = merge_sort_list(head)
    right = merge_sort_list(next_to_middle)

    # Злиття двох відсортованих половин
    sorted_list = merge_sorted_lists(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.value <= right.value:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)

    return result

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

# Для тестування, створимо деякі вузли і зв'яжемо їх в список
node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

# Тестування реверсування списку
reversed_list_head = reverse_list(node1)

# Для візуалізації результату, перетворимо список в Python список
def list_to_array(head):
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    return arr

list_to_array(reversed_list_head)

# Створення списків для тестування
node1 = ListNode(3)
node2 = ListNode(1)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(5)
node4.next = node5

# Тестування сортування злиттям
sorted_list_head = merge_sort_list(node1)
sorted_list = list_to_array(sorted_list_head)

# Тестування об'єднання двох відсортованих списків
merged_list_head = merge_two_sorted_lists(sorted_list_head, node4)
merged_list = list_to_array(merged_list_head)

sorted_list, merged_list
