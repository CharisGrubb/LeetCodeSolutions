#include <bits/stdc++.h>
using namespace std;


// #1 Two Sum 
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for (int i = 0; i< nums.size(); ++i){
            for (int j = 0; j<nums.size(); ++j){
                if (i != j && nums[i] + nums[j] == target){
                    result = {i,j};
                    return  result;
                }
            }
        }
        return result;
    }

};