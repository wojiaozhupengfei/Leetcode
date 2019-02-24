#include <vector>
#include<assert.h>
/**
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

*/
/**
我们来模拟下：
0，【1】
1，【1,1】
2，【1,2,1】
3，【1,3,3,1】
即第i行和第i-1行的关系为
a[i][j] = a[i-1][j-1] + a[i-1][j] 。开头和结尾处为1。不用计算。
*/

class Solution {
public:
	vector<int> getRow(int rowIndex)
	{
		assert(rowIndex <= 33);
		vector<int> row;
		if (rowIndex < 0)
		{
			return row;
		}
		for (int i = 1; i < rowIndex + 1; i++)
		{
			vector<int> buf;
			for (int j = 0; j < i; j++)
			{
				if (i <= 2)
				{
					buf.push_back(1);
				}
				else
				{
					if (j > 0 && j < i - 1)
					{
						int temp = row[j - 1] + row[j];
						buf.push_back(temp);
					}
				}
			}
			row = buf;
		}
		return row;
	}
};