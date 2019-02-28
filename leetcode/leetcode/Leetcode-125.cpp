/**
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false
*/
class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty()) return true;
        int left = 0, right = s.length() - 1;
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        while (left < right)
        {
            if (!isalnum(s[left])) left++;
            else if (!isalnum(s[right])) right--;
            else if (s[left] != s[right]) return false;
            else left++, right--;
        }
        return true;
        
    }
};

