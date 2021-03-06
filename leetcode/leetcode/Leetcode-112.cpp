/**
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

*/
/**
思路，就是每个递归的每个节点的值与当前值比较，所以当前值一定是要减去比较过的节点的值
*/

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
    bool hasPathSum(TreeNode* root, int sum) {
        int i=0;
        if(!root) return false;
        if(!root->left && !root->right && root->val == sum)
        {
            return true;   
        }
        if(hasPathSum(root->left, sum-root->val))
            return true;
        if(hasPathSum(root->right, sum-root->val))
            return true;
        return false;      
    }
};
