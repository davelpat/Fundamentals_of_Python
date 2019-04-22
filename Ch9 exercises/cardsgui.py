"""
Instructions for programming Exercise 9.9

Computer card games are more fun if you can see the images of the cards in a
window, as shown in the screen shot in Figure 9-8.

Assume that the 52 images for a deck of cards are in a DECK folder, with the
file naming scheme <rank number><suit letter>.gif. Thus, for example, the image
for the Ace of Hearts is in a file named 1h.gif, and the image for the King of
Spades is in a file named 13s.gif. Furthermore, there is an image file named
b.gif for the backside image of all the cards.

This will be the card’s image if its faceup variable is False. Using the
DiceDemo program as a role model, write a GUI program that allows you to deal
and view cards from a deck. Be sure to define a helper method that takes a Card
object as an argument and returns its associated image, and remember to turn the
cards as you deal them.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from cards import Card, Deck


