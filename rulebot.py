import re
import random
class RuleBot:
  negative_responses =("no","nope","nah","not a chance","sorry")
  exit_commands =("quit","pause","exit","goodbye","later")
  random_questions =(
      "How can I help you\n?",
      "Ask me something\n",
      "Come on shoot\n"
  )

  def __init__(self):
    self.alienbabble = {'describe_college_intent':r'.*\s*my college.*',
                       'answer_why_intent':r'why\sare.*',
                       'about_tkm':r'.*\s*in tkm'}

  def greet(self):
    self.name = input("What is your name?\n")
    will_help = input(
        f"Hi {self.name}, I am a Rule-Bot.Do you need any help?\n")
    if will_help in self.negative_responses:
      print("OK, have a nice day!")
      return
    self.chat()
  def make_exit(self,reply):
        for command in self.exit_commands:
            if reply == command:
                print("OK, have a nice day")
                return True
  def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
  
  def match_reply(self,reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_college_intent':
                return self.describe_college_intent()
            elif found_match and intent =='answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_tkm':
                return self.about_tkm()
        if not found_match:
            return self.no_match_intent()

  def describe_college_intent(self):
        responses =("TKMCE is situated in kollam\n","It offers btech,barch,mtech,bca and mca courses\n",
                    "It is one of the top ranking engineering colleges in Kerala")
        return random.choice(responses)
  
  def answer_why_intent(self):
        responses = ("I am here to help you to develop your skills\n","I can help you to find ypur area of interest\n",
                     "I will try to answer your queries\n")
        return random.choice(responses)

  def about_tkm(self):
        responses = ("Tkm has lot of tecnical and non techical clubs\n","Each of these clubs aims at improving your skills\n",
                     "Most of the techical clubs do organize workshops and hands sessions\n")
        return random.choice(responses)

  def no_match_intent(self):
        responses = (
            "Please tell me more\n","I am still learning\n","Pardon I didnt get you\n",
            "Sorry I dont know that\n")
        return random.choice(responses)

AlienBot =RuleBot()
AlienBot.greet()