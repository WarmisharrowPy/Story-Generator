import random
books = ['Mother', 'Midnight Children', 'My experiments with truth', 'Mystery']

print(random.choice(books))
Sentence_starter = ['Once upon a time', 'A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
character = [' there lived a king.',' there lived a man named Jack.', ' there lived a farmer.', ' there lived a rabbit.', ' there lived an elephant.', ' there lived a mouse.', ' there lived a turtle.',' there lived a cat.', ' there lived a man named Tom.', ' there lived a man named Jerry.',' there lived a man named Robert.', ' there lived a man named Helgen.', ' there lived a man named Stark.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going to ', ' Barcelona',' India', ' Germany', ' Venice', ' England']
place = [' the mountains', ' the garden', ' cinema', ' university',' seminar', ' school', ' laundry']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 80s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.', ' made a lot of friends',' Eats a burger', ' found a secret key', ' solved a mystery', ' wrote a book']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))
