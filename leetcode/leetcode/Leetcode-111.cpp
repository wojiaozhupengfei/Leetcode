/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/**
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回它的最小深度  2.
*/

/**
这一题和110题中求树的深度很相似，这里直接返回min就好了，但是有一个坑，
就是如果一个根节点只有一个叶子，那么这里要加判断，从有叶子的地方走，去求深度
*/
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        else if (!root->left && !root->right) return 1;
        else if (!root->left&&root->right || root->left&&!root->right)
        {
            root = !root->left?root->right:root->left;
            return minDepth(root)+1;
        }
        int l_depth = minDepth(root->left)+1;
        int r_depth = minDepth(root->right)+1;
        return min(l_depth, r_depth);
    }
};
