#include <vector>
#include<assert.h>
/**
����һ���Ǹ����� k������ k �� 33������������ǵĵ� k �С�

����������У�ÿ�����������Ϸ������Ϸ������ĺ͡�

ʾ��:

����: 3
���: [1,3,3,1]

���ף�

������Ż�����㷨�� O(k) �ռ临�Ӷ���

*/
/**
������ģ���£�
0����1��
1����1,1��
2����1,2,1��
3����1,3,3,1��
����i�к͵�i-1�еĹ�ϵΪ
a[i][j] = a[i-1][j-1] + a[i-1][j] ����ͷ�ͽ�β��Ϊ1�����ü��㡣
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