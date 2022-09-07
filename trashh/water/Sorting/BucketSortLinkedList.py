class Node:
    def __init__(self):
        self.val = None
        self.next = None


def push(head, newVal):
    newEl = Node()
    newEl.val = newVal
    newEl.next = head
    head = newEl
    return head


def getMaxAndMin(head):
    cur = head
    maxval = head.val
    minval = head.val
    while cur != None:
        if cur.val > maxval:
            maxval = cur.val
        if cur.val < minval:
            minval = cur.val
        cur = cur.next
    return maxval, minval


def printNode(head):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next
    print()

def getLen(head):
    curr = head
    count = 0
    while curr != None:
        count += 1
        curr = curr.next
    return count


def insertionLinked(head):
    if head == None or head.next == None:
        return head

    prev_key = head
    key = head.next
    while key != None:
        cur_prev = None
        cur = head
        while cur != key and cur.val <= key.val:
            cur_prev = cur
            cur = cur.next
        if cur.val > key.val:
            prev_key.next = key.next
            if cur_prev == None:
                head = key
                head.next = cur
            else:
                cur_prev.next = key
                key.next = cur
            key = prev_key.next
        else:
            prev_key = key
            key = key.next
    return head


def bucketsortLinked(head):
    if head == None or head.next == None:
        return head

    n = getLen(head)
    high, low = getMaxAndMin(head)
    interval = high-low
    buckets = [None for _ in range(n+1)]
    cur = head
    while cur != None:
        key = int(n* (cur.val-low)/interval)
        if buckets[key] == None:
            buckets[key] = cur
            cur = cur.next
            buckets[key].next = None
        else:
            tmp = cur.next
            cur.next = buckets[key]
            buckets[key] = cur
            cur = tmp
    for bucket in buckets:
        bucket = insertionLinked(bucket)

    result = buckets[n]
    for i in range(n-1, -1, -1):
        if buckets[i] != None:
            tail = buckets[i]
            while tail.next != None:
                tail = tail.next
            tail.next = result
            result = buckets[i]

    return result

