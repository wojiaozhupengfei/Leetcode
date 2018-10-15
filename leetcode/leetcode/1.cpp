#include<stdio.h>
#include<string.h>
#include<stdlib.h>


/**
* Note: The returned array must be malloced, assume caller calls free().
*/
int* twoSum(int* nums, int numsSize, int target) {
	int *result = (int*)malloc(2 * sizeof(int));
	for (int i = 0; i < numsSize; i++)
	{
		for (int j = i + 1; j < numsSize && (j != i); j++)
		{
			if (nums[i] + nums[j] == target)
			{
				result[0] = i;
				result[1] = j;
			}
		}
	}
	return result;
}

void main()
{
	int a[] = { 2, 7, 11, 15 };
	int target = 18;
	int* b = NULL;

	b = twoSum(a, 4, target);
	for (int i = 0; i < 2; i++)
	{
		printf("%d\n", b[i]);
	}

	system("pause");
}