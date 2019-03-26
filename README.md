# Name Generator based on Markov Model
This application will generate names based on 1000 other different names. To be more specific, this application will recognize the patterns and will follow such patterns when generating a new name. If you want to know more, scroll down.


### Here is one example for 10 male names
```
What is the gender for the name?(M/F) "M"
What is the minimum length for the name? 6
What is the maximum length for the name? 10
How many names would you like? 10
Here are 10 novel male names: 
 Gager
 Curien
 Darwilip
 Riuster
 Ayton
 Cadav
 Rieren
 Omill
 Freeni
 Rodney
```
 
### Here is one example for 10 female names

```
What is the gender for the name?(M/F) "F"
What is the minimum length for the name? 6 
What is the maximum length for the name? 10
How many names would you like? 10
Here are 10 novel female names: 
  Narity
  Everacie
  Sicilie
  Mariniya
  Kaylene
  Jayly
  Della
  Camiadley
  Brity
  Kathey
```

### How does this application generate unique names? 
1. Parse the dataset and generate a dictionary that will contain a pair of characters as key and an char array as its value. See code below as an example. 
```
{('al', ['e', 'e', 'i']), ('ol', ['e', 'o', 'i', 'i']), ('le', ['x', 'p', 'f', 'k'])}
```
2. When generating a new name, the application will go through this dictionary until it finds a key that matches current last two characters of new name, and then the way it will select the next letter of the name is by randomly choosing a chracter in a value of this key. 
