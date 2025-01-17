//Authors: Miguel Angel Gama Marroquin und Adrian Graumnitz

//1. Aufgabe
//a)
/**
  * Calculate the windchill temperature
  *
  * @param temperature
  * @param windspeed
  * @return the windchilltemperature
  */
def windchill(temperature: Double, windspeed: Double): Double =
  val windchillTemperature: Double =13.12 + 0.6215 * temperature + (0.3965 * temperature - 11.37) * math.pow(windspeed, 0.16)
  windchillTemperature

//b)
/**
  * Reverse the given list
  *
  * @param acc 
  * @param inputList
  * @return the reversed list
  */
def reverse(inputNumber: Int, acc: Int = 0): Int =
  inputNumber match
    case 0 => acc
    case _=>reverse(inputNumber = inputNumber/10, acc =  10 * acc + inputNumber%10)

//c)

def iteration(list: List[Int]): Int =
  var count:Int = 0
  for (i <- list){
    count += i
  }
  count

//2. Aufgabe
type Time =(Int, Int, Int)
//a)
/**
  * Checks if the given time is valid.
  *
  * @param time a tuple consisting of hours, minutes and seconds
  * @return true if the time is valid, otherwise false
  */
def isTime(time: Time): Boolean =
  val (hour, minute, second) = time
  (hour <= 24 && hour >=0 ) && (minute <= 60 && minute >= 0) && (second <= 60 && second >=0) 

//b)
/**
  * Takes a time and raised by 1 second
  *
  * @param time
  * @return The valid time or a String conluding that time parameter is not valid
  */
def tick(time: Time): Either[Time, String] =
  var (hour, minute, second) = time
  if (hour >= 23 || minute >= 59 || second >= 59){
    var phrase: String = "This is not a valid time"
    return Right(phrase)
  }
  if (second == 59){
    second = 0
    if (minute == 59){
      minute = 0
      if (hour == 23){
        hour = 0
      }
      else{
        hour = hour + 1
      }
    }
    else minute = minute + 1
  }
  else{
    second = second + 1
  }
  Left(hour, minute, second)

//c)
/**
  * Takes a time and reduce it by 1 second
  *
  * @param time
  * @return the reduce time
  */
def kcit(time: Time): Time =
  var (hour, minute, second) = time
  if (second == 0){
    second = 59
    if (minute == 0){
      minute = 59
      if(hour == 0){
        hour = 23
      }
      else{
        hour = hour -1
      }
    }
    else{
      minute = minute -1
    }
  }
  else{
    second = second -1
  }
  (hour,minute, second)

//d)
/**
  * Adds a number of seconds to the given time
  *
  * @param time
  * @param seconds
  * @return time
  */
def addSeconds(time: Time, seconds: Int): Time =
  var (hour, minute, second) = time
  second += seconds
  while(second >= 60){
    second -= 60
    if(minute == 59){
      minute = 0
      if(hour == 23){
        hour = 0
      }
      else{
        hour += 1
      }
    }
    else{
      minute += 1
    }
  }
  (hour, minute, second)

  /**
    * Adds a number of minutes to the given time
    *
    * @param time
    * @param minutes
    * @return time
    */
def addMinutes(time: Time, minutes: Int): Time =
  var (hour, minute, second) = time
  minute += minutes
  while(minute >= 60){
    minute -= 60
    if(hour == 23){
      hour = 0
    }
    else{
      hour += 1
    }

  }
  
  (hour, minute, second)

  /**
    * Adds a number of hours to the given time
    *
    * @param time
    * @param hours
    * @return time
    */
def addHours(time: Time, hours: Int): Time =
  var (hour, minute, second) = time
  hour += hours
  while (hour >= 24){
    hour -= 24
  }
  (hour,minute,second)

//3. Aufgabe
//a)
/**
  * Replace the number with the second parameter if its equal to the first parameter
  *
  * @param symbol_1
  * @param symbol_2
  * @param symbols
  * @return updatet list
  */
def replace[A](symbol_1: A,symbol_2: A, symbols: List[A]): List[A] =
  symbols.map{
    case `symbol_1` => symbol_2
    case other => other
  }

//explicite recursion
/**
  * Replace the number with the second parameter if its equal to the first parameter
  *
  * @param symbol_1
  * @param symbol_2
  * @param symbols
  * @param acc
  * @return updatet list
  */
def replaceRec[A](symbol_1: A, symbol_2: A, symbols: List[A], acc: List[A] = Nil): List[A] =
  symbols match
    case Nil => acc
    case head :: tail if head == symbol_1 => replaceRec(symbol_1, symbol_2, tail, acc :+ symbol_2 )
    case head :: tail => replaceRec(symbol_1, symbol_2, tail,  acc :+ head)

//b)
/**
  * Compares the input list depending on the choosen operator
  *
  * @param comp
  * @param inputList
  * @return true if its comparable or false if its not
  */
def compare[A](comp: (A,A) => Boolean, inputList: List[A]): Boolean =
  inputList match
    case Nil => true
    case  _ :: Nil => true
    case head :: tail => comp(head, tail.head) && compare(comp, tail)

//c)
/**
  * Returns the first `n` elements of a list of integers whose cumulative sum exceeds a given value.
  *
  * @param inputList
  * @param checksum
  * @param borderNumber
  * @param checksumList
  * @return `n` Elements
  */
def takeNumbers(inputList: List[Int], checksum: Int = 0, borderNumber: Int, checksumList: List[Int] = Nil): List[Int] =
  
  if(checksum >= borderNumber){
    checksumList
  }
  else{
    inputList match
      case Nil => checksumList
      case head :: tail => takeNumbers(tail, checksum + head, borderNumber, checksumList :+ head)
  }
  

//d)
/**
  * Recursively folds a list from the right using a binary function.
  *
  * @param f A binary function that combines an element of type A with an accumulator of type B to produce a new accumulator of type B.
  * @param e The recursion anchor
  * @param inputList
  * @return the result of folding the list from the right, of type B
  */
def foldr[A,B](f: (A,B)=>B, e : B, inputList: List[A]): B =
  inputList match
    case Nil => e
    case head :: tail => f(head, foldr(f, e, tail))

/**
  * Reverse an input list with fold right
  * @param inputList
  * @return the reversed list
  */
def reverse2[A](inputList: List[A]): List[A] = foldr((x: A, acc: List[A]) => acc :+ x, Nil, inputList)
@main 
def main(): Unit =
  //a)
  println(windchill(5,10))
  //b)
  println(reverse(inputNumber = 47142))
  //c)
  println(iteration(List(1,2,3)))
  println("\n")
  
  
  println(isTime((1,2,120)))
  println(tick(24,59,59))
  println(kcit((0,0,0)))
  println(addSeconds((23,59,10),120))
  println(addMinutes((22,59,22),2))
  println(addHours((20,5,7),24))

  var symbols = List(1,2,3,4,5,6,7,8,9)

  println(replaceRec(3,4,symbols))
  println(replace(2,3,symbols))
  println(compare((symbol_1: Int, symbol_2: Int) => symbol_1 < symbol_2, symbols))
  println()
  println(takeNumbers(inputList = symbols, borderNumber = 20))

  println(reverse2(symbols))
