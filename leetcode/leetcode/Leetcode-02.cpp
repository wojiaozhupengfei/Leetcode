
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
    //��������ָ��ָ���������������´���һ������洢���
    struct ListNode* p1 = l1;
    struct ListNode* p2 = l2;
    struct ListNode* result = (struct ListNode*)malloc(sizeof(struct ListNode));
    result->val = 0;
    
    //����һ��ָ��ָ�򱣴���
    struct ListNode* p = NULL;//���ָ��ָ��result
    int c = 0;//�洢��ӵĽ�һ
    
    //����Ϊ�ջ��߻��н�һ �Ͳ�����
    while(p1 != NULL || p2 != NULL || c != 0)
    {
        //��pָ��result
        if(p == NULL)
        {
            p = result;
        }
        else//���p�Ѿ�ָ����result����ôp����ָ����һ���ڵ㣬��Ҫ�����ڴ�
        {
            p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            p->next->val = 0;
            p = p->next;
        }
        
        //��������ȡֵ
        int a = (p1 == NULL ? 0 : p1->val);
        int b = (p2 == NULL ? 0 : p2->val);
        
        // ��Ϊ�����е������������еģ�������������
        int s = (a + b + c)%10;
        c = (a + b + c)/10; //�Ƿ��н�һ
        p->val = s;
        
        // ָ����һ������ڵ�
        p1 = (p1 == NULL ? NULL : p1->next);
        p2 = (p2 == NULL ? NULL : p2->next);
    }
    return result;
}

void main()
{

}