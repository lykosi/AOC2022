from wsgiref import validate
from aocd import get_data
from Events.CalorieCounting import CalorieCounting
from Events.RockPaperScissors import RockPaperScissors
from Events.Rucksack import Rucksack

CalorieCounting(get_data(day=1, year=2022))
print("########################################################")
RockPaperScissors(get_data(day=2, year=2022))
print("########################################################")
Rucksack(get_data(day=3, year=2022))
print("########################################################")



