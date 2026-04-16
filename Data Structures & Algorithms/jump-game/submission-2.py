class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        #nodes = indices, edges = jumps possible
        #lst = [i for i in range(len(nums))]
        # goal -> reach the last indes -> return True
        visited = set([0]) 
        que = deque([0])  # possible nodes that can be reached
        while que:
            node = que.popleft()
            #visited.add(node) -> wrong -> dont add to visited when popping, instead add when pushing
            #traverse through all the edges 
            for i in range(1, nums[node]+1):
                nd = node + i
                if nd == len(nums)-1 : #arrived at last index
                    return True
                if nd >= len(nums):
                    continue #ditches the case when it overshoots
                if nd not in visited:
                    visited.add(nd) # add to visited just when you are pushing into que -> else duplicate work
                    que.append(nd)
        return False
                