package kotlin

interface Workable {
    fun work()
}

interface Eatable {
    fun eat()
}

class Human : Workable, Eatable {
    override fun work() {
        println("Working 9 to 5!")
    }

    override fun eat() {
        println("Lunch break time!")
    }
}

class Robot : Workable {
    override fun work() {
        println("Working 24/7!")
    }
}

fun performWork(worker: Workable) {
    worker.work()
}

fun performEat(eater: Eatable) {
    eater.eat()
}

fun main() {
    val human = Human()
    val robot = Robot()

    performWork(human) // Working 9 to 5!
    performEat(human)  // Lunch break time!
    performWork(robot) // Working 24/7!
    // performEat(robot) // Won’t compile – as expected
}
