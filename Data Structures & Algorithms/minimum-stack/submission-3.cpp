#include <iostream>
#include <string>
#include <stack>
#include <memory>
#include <algorithm>

using namespace std;

class MinStack {
    private:
        struct Node {
        int val;
        int minimum;
        unique_ptr<Node> next;

        Node(int val, unique_ptr<Node> next, int prev_value)
            : val(val), next(std::move(next)) {
                this->minimum = std::min(val, prev_value);
        }
    };

public:
    unique_ptr<Node> head;

    MinStack() : head(nullptr) {
    }
    
    void push(int val) {
        int prev_value = (head == nullptr) ? val : head->minimum;
        head = make_unique<Node>(val, std::move(head), prev_value);
    }
    
    void pop() {
        head = std::move(head->next);
    }
    
    int top() {
        return (*head).val;
    }
    
    int getMin() {
        return (*head).minimum;
    }
};