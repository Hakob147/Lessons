# class Person:
#     def __init__(self, age, height, gender):
#         self.age = age
#         self.height = height
#         self.gender = gender
#     def __repr__(self):
#         return f"Age: {self.age}\nHeight: {self.height}\nGender: {self.gender}"
#     def __eq__(self, other):
#         return self.age == other.age
#
# person_1 = Person(25,171,"Male")
# person_2 = Person(25,180,"Female")
# print(person_1 == person_2)

class PlayingCard:
    cards = ("Valet", "Dama", "Karol", "Tuz")
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f"Rank: {self.rank}, Suit: {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.cards.index(self.rank) < self.cards.index(other.rank)

# tt = ("queen", "king")
# print(tt.index("queen"))

card_1 = PlayingCard("Dama", "Qyap")
card_2 = PlayingCard("Valet", "Srti")

print(card_1 < card_2)