# Link
https://leetcode.com/problems/3sum/

# 구현 방법
combination 으로 시도 - 개같이 멸망 - 시간 초과
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    answer = []
    for item in combinations(nums, 3):
        if item[0] + item[1] + item[2] == 0:
            answer.append(list(item))
    return answer
```

# 맞는데 왜 틀리지?
최적화된 방법 사용 - 투 포인트 로직 사용

# 다른 방법
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복 제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
```

# 다른 방법에서 궁금한점

알고리즘 테크닉을 좀 익히자