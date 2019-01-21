#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector< vector<int> > generate(int numRows) {
        vector< vector<int> > res;
        vector<int> current_row;
        if (numRows == 0)
        {
            return res;
        }
        if (numRows == 1)
        {
            //只有一行
            current_row.push_back(1);
            res.push_back(current_row);
            return res;
        }
        current_row.push_back(1);
        res.push_back(current_row);
        int r = 1;
        while(r < numRows)
        {
            r++;
            current_row.clear();
            current_row.push_back(1);
            for (int i = 1; i <r -1; i++)
            {
                current_row.push_back(res[r-2][i-1] + res[r-2][i]);
            }
            current_row.push_back(1);
            res.push_back(current_row);
        }

        return res;
    }
};

int main()
{
    cout << "Hello World!" << endl;
    return 0;
}

