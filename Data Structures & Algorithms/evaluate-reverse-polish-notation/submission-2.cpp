#include <iostream>
#include <string>
#include <stack>
#include <cctype>
#include <cmath>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        stack<int> nums {};
        for (auto it = tokens.begin(); it < tokens.end(); ++it) {
            if (*it == "+" || *it == "-" || *it == "*" || *it == "/" ) {
                int lhs {0};
                int rhs {0};
                switch ((*it)[0]) {
                    case '+':
                        rhs = get_operand(nums);
                        lhs = get_operand(nums);
                        nums.push(lhs + rhs);
                        break;
                    case '*':
                        rhs = get_operand(nums);
                        lhs = get_operand(nums);
                        nums.push(lhs * rhs);
                        break;
                    case '-':
                        rhs = get_operand(nums);
                        lhs = get_operand(nums);
                        nums.push(lhs - rhs);
                        break;
                    case '/':
                        rhs = get_operand(nums);
                        lhs = get_operand(nums);
                        nums.push(lhs / rhs);
                        break;
                }
            } else {
                nums.push(stoi(*it));
            }
        }
        return nums.top();
    }

    int get_operand(stack<int> &nums) {
        int top_val = nums.top();
        nums.pop();
        return top_val;
    }
};