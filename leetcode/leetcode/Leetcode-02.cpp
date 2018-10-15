
#include "stdlib.h"
#include "stdio.h"
#include "string.h"

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode{
    int val;
    struct ListNode * next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    //建立两个指针指向两个链表，并重新创建一个链表存储结果
    struct ListNode* p1 = l1;
    struct ListNode* p2 = l2;
    struct ListNode* result = (struct ListNode*)malloc(sizeof(struct ListNode));
    result->val = 0;
    
    //建立一个指针指向保存结果
    struct ListNode* p = NULL;//这个指针指向result
    int c = 0;//存储相加的进一
    
    //链表不为空或者还有进一 就不结束
    while(p1 != NULL || p2 != NULL || c != 0)
    {
        //将p指向result
        if(p == NULL)
        {
            p = result;
        }
        else//如果p已经指向了result，那么p继续指向下一个节点，需要创建内存
        {
            p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            p->next->val = 0;
            p = p->next;
        }
        
        //从链表中取值
        int a = (p1 == NULL ? 0 : p1->val);
        int b = (p2 == NULL ? 0 : p2->val);
        
        // 因为链表中的数是逆序排列的，所以这样计算
        int s = (a + b + c)%10;
        c = (a + b + c)/10; //是否有进一
        p->val = s;
        
        // 指到下一个链表节点
        p1 = (p1 == NULL ? NULL : p1->next);
        p2 = (p2 == NULL ? NULL : p2->next);
    }
    return result;
}

void main()
{

}