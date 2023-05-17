#ifndef TEST_CASES_H
#define TEST_CASES_H

#include <algorithm>
#include <array>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

std::unordered_map<std::string, int> dictionaryComprehension(const std::vector<std::string>& keys, const std::vector<int>& values);
std::unordered_map<std::string, int> dictionaryInsert(const std::unordered_map<Key, Value>& dict, const std::vector<std::string>& keys, const std::vector<int>& values);
template<typename Key, typename Value>
std::unordered_map<std::string, int> dictionaryMerge(const std::unordered_map<Key, Value>& dictOne, const std::unordered_map<Key, Value>& dictTwo);
template<typename Key, typename Value>
void readDictionaryValues(const std::unordered_map<Key, Value>& dict);

template <typename Iterator>
void iterate(Iterator start, Iterator stop);

template<typename Input, typename Predicate, typename Operation>
std::vector<typename std::result_of<Operation(typename std::iterator_traits<Input>::value_type)>::type> listComprehension(Input first, Input last, Predicate predicate, Operation operation);
std::vector<int> listAppend(std::vector<int> listOne, std::vector<int> listTwo);
void listSort(std::vector<int>& list);

std::set<int> setMerge(const std::set<int>& setOne, const std::set<int>& setTwo);

template<typename Tuple, typename... Args>
auto tupleAppend(const Tuple& tuple, Args&&... args);
template<typename... Args>
auto tupleSort(const std::tuple<Args...>& tuple);
    
#endif
