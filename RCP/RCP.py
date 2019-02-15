import sys, os, random, json, numpy

class RCP_easy():
    def user_input(self,userInput, AI_res):
        if userInput == 'rock' and AI_res == 'scissors':
            return 'WON'
        elif userInput == 'scissors' and AI_res == 'paper':
            return 'WON'
        elif userInput == 'paper' and AI_res == 'rock':
            return 'WON'
        elif userInput == AI_res:
            pass
        else:
            return 'LOST'
    def AI_answer(self, userInput = None):
        answers = ['rock', 'scissors', 'paper']
        return answers[random.randint(-1,2)]

class RCP_medium():
    def ai_answer(self,name):
        with open('db.json') as json_file:
            data = json.load(json_file)
        maxim = (data[name]['medium'].index(max(data[name]['medium'])))
        if maxim == 0:
            return 'paper'
        elif maxim == 1:
            return 'rock'
        else:
            return 'scissors'
    
    def increment_db(self,name, choice):
        with open('db.json', 'r+') as json_file:
            data = json.load(json_file)
            
            if choice == 'rock':
                data[name]['medium'][0] += 1

            elif choice == 'scissors':
                data[name]['medium'][1] += 1
            
            else:
                data[name]['medium'][2] += 1
            json_file.seek(0)
            json.dump(data,json_file, indent = 4)
            json_file.truncate()

        

    def user_input(self,userInput,AI_res,name):
        if userInput == 'rock' and self.ai_answer(name) == 'scissors':
            self.increment_db(name,'rock')
            return 'WON'
        elif userInput == 'scissors' and self.ai_answer(name) == 'paper':
            self.increment_db(name,'scissors')
            return 'WON'
        elif userInput == 'paper' and self.ai_answer(name) == 'rock':
            self.increment_db(name,'paper')
            return 'WON'
        elif userInput == self.ai_answer(name):
            if userInput == 'rock':
                self.increment_db(name,'rock')
            elif userInput == 'scissors':
                self.increment_db(name,'scissors')
            else:
                self.increment_db(name,'paper')
            pass
        else:
            if userInput == 'rock':
                self.increment_db(name,'rock')
            elif userInput == 'scissors':
                self.increment_db(name,'scissors')
            else:
                self.increment_db(name,'paper')
            return 'LOST'
    

class RCP_hard():
    last_move = 'rock'
    def aiHard_answer(self,name):
        with open('db.json') as json_file:
            data = json.load(json_file)
        maxim = (data[name]['hard'][self.last_move].index(max(data[name]['hard'][self.last_move])))
        minim = (data[name]['hard'][self.last_move].index(min(data[name]['hard'][self.last_move])))
        if maxim == 0 and minim == 1:
            return random.choice(['rock', 'paper'])
        elif maxim == 0 and minim == 2:
            return random.choice(['rock', 'scissors'])
        elif maxim == 1 and minim == 0:
            return random.choice(['scissors', 'paper'])
        elif maxim == 1 and minim == 2:
            return random.choice(['scissors', 'rock'])
        elif maxim == 2 and minim == 0:
            return random.choice(['scissors', 'paper'])
        else:
            return random.choice(['paper', 'rock'])
    
    def increment_dbHard(self,name,choice):
        with open('db.json', 'r+') as json_file:
            data = json.load(json_file)
        
            if choice =='rock':
                 data[name]['hard'][self.last_move][0] += 1
            elif choice =='scissors':
                data[name]['hard'][self.last_move][1] += 1
            else:
                data[name]['hard'][self.last_move][2] += 1
            json_file.seek(0)
            json.dump(data,json_file, indent = 4)
            json_file.truncate()


    def user_input(self,userInput,AI_res,name):
        #print(self.last_move)
        if userInput =='rock' and self.aiHard_answer(name) == 'scissors':
            self.increment_dbHard(name,'rock')
            self.last_move = userInput
            return 'WON'
        elif userInput == 'scissors' and self.aiHard_answer(name) == 'paper':
            self.increment_dbHard(name,'scissors')
            self.last_move = userInput
            return 'WON'
        elif userInput == 'paper' and self.aiHard_answer(name) == 'rock':
            self.increment_dbHard(name,'paper')
            self.last_move = userInput
            return 'WON'
        elif userInput == self.aiHard_answer(name):
            if userInput == 'rock':
                self.increment_dbHard(name,'rock')
                self.last_move = userInput
            elif userInput == 'scissors':
                self.increment_dbHard(name,'scissors')
                self.last_move = userInput
            else:
                self.increment_dbHard(name,'paper')
                self.last_move = userInput
            pass
        else:
            if userInput == 'rock':
                self.increment_dbHard(name,'rock')
                self.last_move = userInput
            elif userInput == 'scissors':
                self.increment_dbHard(name,'scissors')
                self.last_move = userInput
            else:
                self.increment_dbHard(name,'paper')
                self.last_move = userInput
            return 'LOST'

    
class Users():
    def __init__(self):
        if os.path.exists('db.json'):
            with open('db.json') as json_file:
                self.db = json.load(json_file)
        else:
            self.db = {}

    def create_db(self):
        with open('db.json','w') as outfile:
            json.dump(self.db,outfile,sort_keys = True, indent = 4)

    def add_player(self,name):
        if name not in self.db:
            self.db[name]= {}
            self.db[name]['medium'] = [0,0,0]
            self.db[name]['hard'] = {"rock":[0,0,0],"scissors":[0,0,0],"paper":[0,0,0]}
            self.create_db()
            return True
        else:
            return False

    def load_player(self, name):
        if name not in self.db:
            return False
        else:
            return True
    
    def add_statistics(self, name, difficulty, values):
        self.db[name][difficulty] = values
        self.create_db()
        
        

#if __name__ == "__main__":
    # b = RCP_medium()
    #c = RCP_hard()
    #c.matrice()
    #   b.read_db('ghita')
    # b.increment_db('bute', 'paper')
    # a = Users()
    # a.create_db()
    # a.add_player('ghita')
    # a.add_statistics('ghita', 'medium', [1,5,4])


