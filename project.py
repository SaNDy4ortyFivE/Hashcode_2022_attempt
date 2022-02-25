class Project:
        def __init__(self, project_name, days, score, deadline, roles):
                self.__project_name = project_name
                self.__days = days
                self.__score = score
                self.__deadline = deadline
                self.__roles = []
                for r in roles:
                        self.__roles.append(r)
                
        def getProjectName(self):
                return self.__project_name
        
        def getDays(self):
                return self.__days
        
        def getScore(self):
                return self.__score
                
        def getDeadline(self):
                return self.__deadline
                
        def getRoles(self):
                return self.__roles
                
        def getTotalRoles(self):
                return len(self.__roles)

