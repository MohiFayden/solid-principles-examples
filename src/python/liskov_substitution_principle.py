from abc import ABC, abstractmethod


class Bird(ABC):
    def make_sound(self):
        print("Chirp chirp!")


class FlyingBird(Bird):
    def fly(self):
        print("I can fly!")


class Penguin(Bird):
    def swim(self):
        print("I can swim!")


def move_bird(bird: Bird):
    bird.make_sound()


def let_bird_fly(bird: Bird):
    if isinstance(bird, FlyingBird):
        bird.fly()
    else:
        print("This bird can't fly.")


# Usage
move_bird(FlyingBird())  # Chirp chirp!
move_bird(Penguin())  # Chirp chirp!
let_bird_fly(FlyingBird())  # I can fly!
let_bird_fly(Penguin())  # This bird can't fly.
