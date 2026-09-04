#include <iostream>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> opens;
        for (auto const &character : s) {
            if (is_open(character)) {
                opens.push(character);
            } else {
                if (!opens.empty()) {
                    if (character != get_pair(opens.top())) {
                        return false;
                    }
                    opens.pop();
                } else {
                    return false;
                }
            }
        }
        return opens.empty();
    }
private:
    bool is_open(const char &character) {
        return (character == '[' || character == '{' || character == '(');
    }

    char get_pair(const char &character) {
        switch (character) {
            case '[':
                return ']';
            case '{':
                return '}';
            case '(':
                return ')';
        }
        return '1';
    }
};