import java.util.Random
//Exercise 11
//Authors: Miguel Angel Gama Marroquin and Adrian Graumnitz

//1.
/**
  * Approximates the value of π using the Monte Carlo method
  *
  * @param number The number of random points to generate.
  */
def monteCarlo(number: Int ): Unit =
  var smallerOrEqual: Int = 0
  var approximation: Float = 0
  var random: Random = new Random()
  
  for (i<- 1 to number){
    if(math.pow(random.nextFloat(),2)+math.pow(random.nextFloat(),2) <= 1){
      smallerOrEqual += 1
    }
  }
  approximation = 4* (smallerOrEqual.toFloat/number)
  println(s"smaller or equal to 1: $smallerOrEqual, Approximation: ($approximation")

//2a and 2b
/**
  * The `LicensePlate` object is responsible for generating license plate numbers
  * 
  * @return A string representing a unique license plate number
  */
object LicensePlate {
    private var counter: Int = 0
    def generateLicenseNumber(): String = {
      counter += 1
      s"Ber$counter"  
    }
  }
  
  /**
    * The `Car` class represents a car with specific attributes and behaviors
    *
    * @param wheel
    * @param door
    * @param accelerate
    * @param color
    * 
    * The class provides methods to drive the car, increase speed, decrease speed (with some constraints), and print the car's license number
    * 
    */
  class Car(var wheel: Int, var door: Int, var accelerate: Int, var color: String) {
    val licenseNumber: String = LicensePlate.generateLicenseNumber()
   
    def drive(): Unit = 
      this.accelerate = 10
      println("Car starts to drive")
      println(s"The Car has a speed of $accelerate")
    
    def faster(): Unit = 
      this.accelerate += 10
    
    def slower(): Unit = 
      if (this.accelerate == 0 || this.accelerate - 10 <= 0) {
        println("The car can't drive slower")
      } else {
        this.accelerate -= 10
        println(s"The Car has a speed of $accelerate")
      }
    
    def printLicenseNumber(): Unit = 
      println(s"The license number of this car is $licenseNumber")
    
    def maxSpeed(): Unit =
      println(s"The max speed of the cars are 200")
  }
  
/**
  * The `FastCar` class represents a specialized type of `Car` that overrides the `maxSpeed` method 
  *
  * @param wheel
  * @param door
  * @param accelerate
  * @param color
  */
class FastCar(wheel: Int, door: Int, accelerate: Int, color: String) extends Car(wheel, door, accelerate, color){
 
  override def maxSpeed(): Unit = 
    println(s"The max speed of the fast cars are 300")
}

/**
  * The `SlowCar` class represents a specialized type of `Car` that overrides the `maxSpeed` method 
  *
  * @param wheel
  * @param door
  * @param speed
  * @param color
  */
class SlowCar(wheel: Int, door: Int, speed: Int, color: String) extends Car(wheel, door, speed, color){
  override def maxSpeed(): Unit = 
    println(s"The max speed of the fast cars are 100")
}

/**
  * The `MediumSpeedCar` class represents a specialized type of `Car` that overrides the `maxSpeed` method 
  *
  * @param wheel
  * @param door
  * @param accelerate
  * @param color
  */
class MediumSpeedCar(wheel: Int, door: Int, accelerate: Int, color: String) extends Car(wheel, door, accelerate, color){
  override def maxSpeed(): Unit = 
    println(s"The max speed of the fast cars are 150")
}


@main def main(): Unit = 
  //1)
  monteCarlo(1000)
  
  //2a,b)
  val toyota = new Car(4, 4, 120, "Green")
  toyota.drive()
  toyota.faster()
  toyota.slower()
  toyota.slower()
  println(toyota.color)
  toyota.printLicenseNumber()  
  val mazda = new Car(4, 6, 100, "Yellow")
  mazda.printLicenseNumber()  
  val fiat = new Car(4, 4, 110, "Violet")
  fiat.printLicenseNumber()  

  val chrysler = new Car(4, 5, 90, "Pink")
  chrysler.printLicenseNumber()  

  //2c)
  chrysler.maxSpeed()
  val racingCar = FastCar(4,2,100, "red")
  racingCar.maxSpeed()
  val mediumSpeedCar = MediumSpeedCar(4,4,50, "Blue")
  mediumSpeedCar.maxSpeed()
  val slowCar = SlowCar(4,4,20,"Grey")
  slowCar.maxSpeed()