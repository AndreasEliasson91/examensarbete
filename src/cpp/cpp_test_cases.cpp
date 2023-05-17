#include "test_cases.h"


std::unordered_map<std::string, int> dictionaryComprehension(const std::vector<std::string>& keys, const std::vector<int>& values) {
    std::unordered_map<std::string, int> dict;

    if (keys.size() != values.size())
        return dict; // Return empty "dictionary" if keys and values are not the same size

    for (size_t i=0; i < keys.size(); i++)
        dict[keys[i]] = values[i];

    return dict;
}
template<typename Key, typename Value>
std::unordered_map<std::string, int> dictionaryInsert(const std::unordered_map<Key, Value>& dict, const std::vector<std::string>& keys, const std::vector<int>& values) {
    for (size_t i=0; i < keys.size(); i++)
        dict[keys[i]] = values[i];

    return dict;
}
template<typename Key, typename Value>
std::unordered_map<std::string, int> dictionaryMerge(const std::unordered_map<Key, Value>& dictOne, const std::unordered_map<Key, Value>& dictTwo) {
    std::unordered_map<Key, value> mergedDict = dictOne;

    for (const auto& dictPair : dictTwo)
        mergedDict[dictPair.first] = dictPair.second;

    return mergedDict;
}
template<typename Key, typename Value>
void readDictionaryValues(const std::unordered_map<Key, Value>& dict) {
    for (const auto& dictPair : dict)
        const Value& value = dictPair.second;
}

template <typename Iterator>
void iterate(Iterator start, Iterator stop) {
    for (auto i=start; i != end; i++)
        ;
}

template<typename Input, typename Predicate, typename Operation>
std::vector<typename std::result_of<Operation(typename std::iterator_traits<Input>::value_type)>::type> listComprehension(Input first, Input last, Predicate predicate, Operation operation) {
    using ResultType = typename std::result_of<Operation(typename std::iterator_traits<Input>::value_type)>::type;
    std::vector<ResultType> result;

    std::transform(first, last, std::back_inserter(result), [&](const auto& value) {
        return predicate(value) ? operation(value) : ResultType{};
    });

    return result;
}
std::vector<int> listAppend(std::vector<int> listOne, std::vector<int> listTwo) {
    
}
void listSort(std::vector<int>& list) {
    std::sort(list.begin(), list.end());
}

std::set<int> setMerge(const std::set<int>& setOne, const std::set<int>& setTwo) {
    std::set<int> mergedSet = setOne;
    mergedSet.insert(setTwo.begin(), setTwo.end());

    return mergedSet;
}

template<typename Tuple, typename... Args>
auto tupleAppend(const Tuple& tuple, Args&&... args) {
    return std::tuple_cat(tuple, std::make_tuple(std::forward<Args>(args)...));
}
template<typename... Args>
auto tupleSort(const std::tuple<Args...>& tuple) {
    std::array<int, sizeof...(Args)> tmp{tuple};
    std::sort(tmp.begin(), tmp.end())MAX_READ_LOCKS

    return std::make_tuple(tmp);
}
