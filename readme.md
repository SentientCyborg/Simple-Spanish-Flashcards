# Simple Spanish Flashcards

This is a program to generate simple flash cards for Spanish words. Each card is shown 
on screen for three seconds. Then the card flips to the answer. If you guessed the card 
correctly, you can press the green check, and the card will be removed from the list of 
cards to learn, and a new word will be added.

The included csv file contains 1000 words (and their translations), 
but the program will only reference 100 words at a time. **Please note the translations
came from Google Translate, and they may not be accurate.** 

If you want to use this to learn a different language, supply a new
csv file and add it to the "data" folder. Then update the code on lines
40-42. The language names must be exactly the same as they are listed on 
the new CSV file, or an error will occur. 


---

![Example Front](https://github.com/SentientCyborg/Simple-Spanish-Flashcards/blob/main/images/example_front.png)
![Example Back](https://github.com/SentientCyborg/Simple-Spanish-Flashcards/blob/main/images/example_back.png)



---

This code was written as part of the Capstone project for Day 31 of the 
Udemy course [100 Days of Code by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/). 
This code is similar to the instructor's final version, but includes changes that were not discussed in 
the lessons or the answer walkthrough. 

---

Source for [Spanish Words](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish1000)

---

To run this code, you will need Python 3 with Pandas. 

--Coded using Python 3.8.6
