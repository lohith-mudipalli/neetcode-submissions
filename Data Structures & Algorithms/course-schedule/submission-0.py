class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = {}

        for course in range(numCourses):
            prereq[course] = []

        for course, prerequisite in prerequisites:
            prereq[course].append(prerequisite)

        path = set()

        def dfs(course):

            if course in path:
                return False

            if prereq[course] == []:
                return True

            path.add(course)

            for prerequisite in prereq[course]:
                if not dfs(prerequisite):
                    return False
                
            path.remove(course)

            prereq[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        