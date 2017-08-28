package Week1;

import java.util.ArrayList;

import DataStructures.ListNode;

public class ReverseLinkedList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ListNode node = new ListNode(1);
		ListNode root = node;
		for(int i = 2; i<=8;i++){
			node.next = new ListNode(i);
			node = node.next;
		}
		node.next = null;
		ListNode t = root;
		ListNode.printList(t);
		t = reverseBetween(root,2, 4);
		ListNode.printList(t);
		
	}
	
	public static ArrayList<ListNode> reverse(ListNode p, ListNode head, ListNode tail) {
		
		ListNode prev, curr, next;
		ArrayList<ListNode> nodes = new ArrayList<ListNode>();
		prev = p;
		curr = head;
		next = curr.next;
		ListNode temp = head;
		
		while(curr.next!=tail.next){
			curr.next = prev;
			prev = curr;
			curr = next;
			next = next.next;
		}
		head = curr;
		ListNode.printList(head);
		nodes.add(head);
		nodes.add(temp);
        return nodes;
    }
	
	public static ListNode reverseBetween(ListNode head, int m, int n){
		
		int count = 1;
		ListNode curr, prev_m = null, next_n = null, m_node=null, n_node=null;
		curr = head;
		
		while(curr!=null){
			if(count==m-1){
				prev_m = curr;
				m_node = curr.next;
				break;
			}
			curr=curr.next;
			count++;
			
		}
		
		count = 1;
		curr = head;
		while(curr!=null){
			if(count==n){
				next_n = curr.next;
				n_node = curr;
				break;
			}
			curr=curr.next;
			count++;
		}
		
		System.out.println("prev_m is "+prev_m.val);
		System.out.println("m_node is "+m_node.val);
		
		System.out.println("next_n is "+next_n.val);
		System.out.println("n_node is "+n_node.val);
		ArrayList<ListNode> nodes = reverse(prev_m, m_node, n_node);
		m_node = nodes.get(0);
		
		ListNode.printList(m_node);
		
		System.out.println("Now the head is - "+m_node.val);
		prev_m.next = m_node;
		n_node = nodes.get(1);
		System.out.println("Now the tail is - "+n_node.val);
		
		prev_m.next = m_node;
		n_node.next = next_n;
		
		return head;
	}
}
