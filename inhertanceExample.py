class Game:
    def part1Name(self,s):
        self.name = s
        print(s)
    def CharacterNameInPart1(self,CharacterName):
        self.C_name =CharacterName
        print(CharacterName)


class Game1(Game):

    def part2Name(self,s):
        self.Name = s
        print(s)
    def CharacterNameInPart2(self, CharacterName):
        self.C_name = CharacterName
        print(CharacterName)

obj = Game()
obj.part1Name("Prototype1")
obj.CharacterNameInPart1("AlexMercer")

obj1 = Game1()
obj1.part2Name("Prototype2")
obj1.CharacterNameInPart2("JamesHeller")


#//input[@id="username"]
#//input[@name = "session_key"]
#//input[@aria-describedby= "error-for-username"]
#//input[@aria-label ="Email or phone"]
#//input[@type = "text"]
# //input[@id='username']
# //input[contains(@id,'username')]
# //input[contains(@aria-label,'Email')]