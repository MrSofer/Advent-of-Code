#include <iostream>
#include <fstream>
#include <vector>
#include <string>

long long power(long long base, long long exp) {
    long long res = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            res *= base;
        }
        base *= base;
        exp /= 2;
    }
    return res;
}

std::vector<int> find_max_digit(const std::string& line,const int start,const int end)
{
    std::vector<int> res;
    int max_digit = line[start] - '0';
    int max_digit_index = start;
    for (int i = start + 1; i < end ; ++i)
    {
        int curr_digit = line[i] - '0';
        if (max_digit < curr_digit) {max_digit = curr_digit; max_digit_index = i;}
    }
    res.push_back(max_digit);
    res.push_back(max_digit_index);
    return res;
}

long long get_to_add(const std::string& line, int length)
{
    long long total = 0;
    int start = 0;
    while (length > 0)
    {
        std::vector<int> curr_digit = find_max_digit(line,start,line.size() + 1 - length);
        start = curr_digit.at(1) + 1;
        total += curr_digit.at(0) * power(10,length-1);

        --length;
    }
    return total;
}

int main()
{
    std::ifstream file("input.txt");

    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file." << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;

    long long ret = 0;

    while (std::getline(file, line)) {

        const long long to_add = get_to_add(line,12);
        ret += to_add;
    }

    file.close();
    std::cout << ret;
    return 0;
}



#include "Joltage.h"