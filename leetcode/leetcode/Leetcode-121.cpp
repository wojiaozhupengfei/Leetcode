#include<vector.h>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0)
        {
            return 0;
        }
        int min = prices[0];
        int max = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            if (min < prices[i])
            {
                max = max > (prices[i] - min) ? max : (prices[i] - min);
            }
            else
            {
                min = prices[i];
            }
            
        }
        return max;
    }
};