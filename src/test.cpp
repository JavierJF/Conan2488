#include <test.h>

optional<int> greaterThanFive(int n) {
    if (n > 5) {
        return n;
    } else {
        return {};
    }
}