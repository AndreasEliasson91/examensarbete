#ifndef GENERATOR_H
#define GENERATOR_H

#include <iostream>

class Generator {
private:
    int end;

public:
    explicit Generator(int end) : end(end) {}

    class Iterator {
    private:
        int currentValue;

    public:
        using iterator_category = std::input_iterator_tag;
        using value_type = int;
        using difference_type = int;
        using pointer = int*;
        using reference = int&;

        Iterator(int currentValue) : currentValue(currentValue) {}

        reference operator*() { return currentValue; }
        pointer operator->() { return &currentValue; }
        Iterator& operator++() { ++currentValue; return *this; }
        Iterator operator++(int) { Iterator copy(*this); ++currentValue; return copy; }
        bool operator==(const Iterator& other) const { return currentValue == other.currentValue; }
        bool operator!=(const Iterator& other) const { return !(*this == other); }
    };

    Iterator begin() const { return Iterator(0); }
    Iterator end() const { return Iterator(end); }

};

Generator generatorSequence(int end) { return Generator(end); }

#endif
