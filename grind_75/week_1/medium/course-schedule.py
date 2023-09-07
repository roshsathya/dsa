# https://leetcode.com/problems/course-schedule/

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        inward_course_dict = {i: 0 for i in range(numCourses)}
        dependency_dict = {}
        
        for course, dependent in prerequisites:
            if dependent not in dependency_dict:
                dependency_dict[dependent] = []
            dependency_dict[dependent].append(course)
            inward_course_dict[course] += 1

        for course, value in inward_course_dict.items():
            if value == 0:
                queue.append(course)

        while True:
            try:
                curr_course = queue.popleft()
            except:
                break
            dependents = dependency_dict.get(curr_course, [])
            for dependent in dependents:
                inward_course_dict[dependent] -= 1
                if inward_course_dict[dependent] == 0:
                    queue.append(dependent)

        for course, value in inward_course_dict.items():
            if value == 1:
                return False
        return True
         
