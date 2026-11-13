#include "Forklift.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

const std::string PATH = "input.txt";

std::vector<std::string> get_input(const std::string & path)
{
    std::vector<std::string> input;
    std::ifstream file(path);

    if (!file.is_open())
    {
        std::cerr << "Error: Could not open the file" << std::endl;
    }
    else
    {
        std::string line;
        while (std::getline(file,line))
        {
            input.push_back(line);
        }
    }

    return input;
}

std::vector<std::vector<int>> count_adjacent_rolls(const std::vector<std::string> &input,const size_t m,const size_t n)
{

    auto adjacent_rolls = std::vector(m,std::vector<int>(n));

    for (size_t i = 0 ; i < m ; ++i)
    {
        for (size_t j = 0 ; j < n ; ++j)
        {
            if (input.at(i).at(j) == '@')
            {
                if (i > 0)
                {
                    if (j > 0) {adjacent_rolls.at(i-1).at(j-1)++;}
                    adjacent_rolls.at(i-1).at(j)++;
                    if (j < n-1) {adjacent_rolls.at(i-1).at(j+1)++;}
                }
                if (j > 0) {adjacent_rolls.at(i).at(j-1)++;}
                if (j < n-1) {adjacent_rolls.at(i).at(j+1)++;}
                if (i < m-1)
                {
                    if (j > 0) {adjacent_rolls.at(i+1).at(j-1)++;}
                    adjacent_rolls.at(i+1).at(j)++;
                    if (j < n-1) {adjacent_rolls.at(i+1).at(j+1)++;}
                }
            }
        }
    }



    return adjacent_rolls;
}

void remove_adjacent_count(std::vector<std::string> &input, std::vector<std::vector<int>> &adjacent_rolls, const size_t m, const size_t n)

{
    for (size_t i = 0 ; i < m ; ++i)
    {
        for (size_t j = 0 ; j < n ; ++j)
        {
            if (input.at(i).at(j) == 'x')
            {
                if (i > 0)
                {
                    if (j > 0) {adjacent_rolls.at(i-1).at(j-1)--;}
                    adjacent_rolls.at(i-1).at(j)--;
                    if (j < n-1) {adjacent_rolls.at(i-1).at(j+1)--;}
                }
                if (j > 0) {adjacent_rolls.at(i).at(j-1)--;}
                if (j < n-1) {adjacent_rolls.at(i).at(j+1)--;}
                if (i < m-1)
                {
                    if (j > 0) {adjacent_rolls.at(i+1).at(j-1)--;}
                    adjacent_rolls.at(i+1).at(j)--;
                    if (j < n-1) {adjacent_rolls.at(i+1).at(j+1)--;}
                }
                input.at(i).at(j) = '.';
            }
        }
    }
}

int increment_valid_papers(std::vector<std::string> &input, const std::vector<std::vector<int>> &adjacent_rolls, const size_t m, const size_t n)
{
    int to_add = 0;
    for (size_t i = 0 ; i < m ; ++i)
    {
        for (size_t j = 0 ; j < n ; ++j)
        {
            if (input.at(i).at(j) == '@' && adjacent_rolls.at(i).at(j) < 4)
            {
                to_add++;
                input.at(i).at(j) = 'x';
            }
        }
    }
    return to_add;
}

int main()
{
    auto input = get_input(PATH);

    const size_t m = input.size() , n = input.at(0).size();

    auto adjacent_rolls = count_adjacent_rolls(input,m,n);

    int total = 0;

    int to_add = increment_valid_papers(input,adjacent_rolls,m,n);
    total+= to_add;

    while (to_add > 0)
    {
        remove_adjacent_count(input,adjacent_rolls,m,n);
        to_add = increment_valid_papers(input,adjacent_rolls,m,n);
        total += to_add;
    }



    std::cout << "Total amount of rolls that can be accessed by the forklift is " << total << std::endl;

    return 0;
}