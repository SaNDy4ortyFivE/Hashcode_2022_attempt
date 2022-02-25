class Contributor:
        def __init__(self, name, total_skills, skills):
                self.__name = name
                self.__total_skills = total_skills
                self.__skills = []
                for skill in skills:
                        self.__skills.append(skill)
                self.__isAssigned = False
                        
        def getName(self):
                return self.__name
                
        def getSkills(self):
                return self.__skills
        
        def getTotalSkills(self):
                return self.__total_skills
                
        def assignWork(self):
                print("Assigning work to {}".format(self.__name))
                self.__isAssigned = True
                
        def deassignWork(self):
                print("Releasing from  work ({})".format(self.__name))
                self.__isAssigned = False
                
        def getStatus(self):
                return self.__isAssigned
                
        def getContributorSkillLevel(self, skillName):
                l = 0;
                for s in self.__skills:
                        if s.getSkill() == skillName:
                                l = s.getLevel()
                                break
                return l
        
        def upgradeSkill(self, skillName):
                for s in self.__skills:
                        if s.getSkill() == skillName:
                                s.incrementLevel()
                                break

