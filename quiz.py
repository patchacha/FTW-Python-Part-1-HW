# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:18:56 2020

@author: ppangatungan
"""

Question1 = """What is the highest mountain in the Philippines?
A. Pulag
B. Halcon
C. Apo
Answer: """

Question2 = """What is the smallest province in the Philippines?
A. Siquijor
B. Batanes
C. Dinagat
Answer: """

Question3 = """Which province in the Philippines has the largest population?
A. Laguna
B. Cebu
C. Cavite
Answer: """

Question4 = """Which city in the Philippines is the richest in terms of assets?
A. Taguig
B. Makati
C. Pasig
Answer: """

Question5 = """What continent is the Philippines in?
A. Europe
B. Asia 
C. Australia
Answer: """

Question6 = """What religion is more prominent in the Philippines?
A. Buddhism
B. Muslim
C. Roman Catholic
Answer: """

Question7 = """What is the Philippines' national flower?
A. Sampaguita
B. Waling-Waling
C. Bougainvillea
Answer: """

Question8 = """What is the Philippines' national tree?
A. Yakal
B. Narra
C. Molave
Answer: """

Question9 = """What is the Philippines' national bird?
A. Maya
B. Philippine Eagle
C. Philippine Cockatoo
Answer: """

Question10 = """What is the Philippines' national animal?
A. Tarsier
B. Carabao
C. Tamaraw
Answer: """

point = 0

name = input("Please enter your name: ")
print('Hello ' + name.title() + '! Welcome to a Quiz about the Philippines. How well do you know our country? Type the letter of your answer.')

mc = {Question1:"C", Question2:"B", Question3:"B", Question4:"B", Question5:"B", Question6:"C", Question7:"A", Question8:"B", Question9:"B", Question10:"B"}

for question in mc:
    answer = input(question)
    if answer.title() == mc[question]:
        point += 1
        
score = (point/len(mc))*100

print('\nHi '+ name.title() + '!')
if score >= 70:
    print("Congratulations!\nYou know the Philippines so well!\nYou got",point,"over",len(mc),"or",score,"%")
else:
    print("Oh no. You still have a lot to learn about our country.\nYou got",point,"over",len(mc),"or",score,"%")        