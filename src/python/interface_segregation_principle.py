from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        print("Working 9 to 5!")

    def eat(self):
        print("Lunch break time!")


class Robot(Workable):
    def work(self):
        print("Working 24/7!")


# Usage
def perform_work(worker: Workable):
    worker.work()


def perform_eat(eater: Eatable):
    eater.eat()


perform_work(Human())  # Working 9 to 5!
perform_eat(Human())  # Lunch break time!
perform_work(Robot())  # Working 24/7!
# perform_eat(Robot()) # This would raise an error
