/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;

        if (current != null) {
            while (current.next != null) {
                if (prev == null) {
                    prev = new ListNode(current.val, null);
                    current = current.next;
                    continue;
                }
                ListNode temp = new ListNode(current.val, prev);
                prev = temp;
                current = current.next;
            }
            return new ListNode(current.val, prev);
        }
        return null;
    }
}