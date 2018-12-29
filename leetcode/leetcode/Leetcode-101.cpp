/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        else
            return isMirrioTree(root->left, root->right);
    }
public:
    bool isMirrioTree(TreeNode* q, TreeNode* p)
    {
        if (q == NULL && p == NULL)
            return true;
        else if (q != NULL && p != NULL)
        {
            if (q->val != p->val)
                return false;
            else
            {
                return isMirrioTree(q->left, p->right) && isMirrioTree(q->right, p->left);
            }
        }
        else
            return false;
    }
};
