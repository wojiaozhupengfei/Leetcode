class Solution{
public:
    int maxprofit(vector<int>& prices)
    {
		int valley, peak, index = 0, maxprofit = 0;
		int len = prices.size();
		while(index < len - 1)
		{
			//寻找波谷
			while(index < len -1 && prices[index] >= prices[index + 1])
			{
				index++;
			}
			valley = prices[index];
			//寻找波峰
			while(index < len -1 && prices[index] <= prices[index + 1])
			{
				index ++;
			}
			peak = prices[index];
			maxprofit += peak - valley;
		}
		return maxprofit;
    } 
};
