package kotlin

open class Bird {
    fun makeSound() {
        println("Chirp chirp!")
    }
}

class FlyingBird : Bird() {
    fun fly() {
        println("I can fly!")
    }
}

class Penguin : Bird() {
    fun swim() {
        println("I can swim!")
    }
}

fun moveBird(bird: Bird) {
    bird.makeSound()
}

fun letBirdFly(bird: Bird) {
    if (bird is FlyingBird) {
        bird.fly()
    } else {
        println("This bird can't fly.")
    }
}

// Usage
fun main() {
    moveBird(FlyingBird())   // Chirp chirp!
    moveBird(Penguin())      // Chirp chirp!
    letBirdFly(FlyingBird()) // I can fly!
    letBirdFly(Penguin())    // This bird can't fly.
}
