class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        atual = head
        tamanho = 0

        while atual is not None:
            tamanho += 1
            atual = atual.next

        meioIndex = tamanho // 2

        meioNode = head

        for i in range(meioIndex):
            meioNode = meioNode.next

        return meioNode