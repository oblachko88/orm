#include <iostream>

class Node {
public:
    int data;
    Node* next;

    Node(int value) : data(value), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;



public:
    LinkedList() : head(nullptr) {}

    void insertNode(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }

    void displayList() {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }


    void reverseList() {
        Node* prev = nullptr;
        Node* current = head;
        Node* nextNode = nullptr;

        while (current != nullptr) {
            nextNode = current->next;
            current->next = prev;
            prev = current;
            current = nextNode;
        }

        head = prev;
    }
    
    
    ~LinkedList() {
        Node* current = head;
        Node* nextNode = nullptr;

        while (current != nullptr) {
            nextNode = current->next;
            delete current;
            current = nextNode;
        }
    }
};

int main() {
    LinkedList myList;


    myList.insertNode(10);
    myList.insertNode(20);
    myList.insertNode(30);

    std::cout << "Original List: ";
    myList.displayList();

    myList.reverseList();

    std::cout << "Reversed List: ";
    myList.displayList();

    return 0;
}