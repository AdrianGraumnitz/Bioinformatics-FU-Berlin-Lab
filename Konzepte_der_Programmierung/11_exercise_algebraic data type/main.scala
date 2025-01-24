//Exercise 11
//Autors: Miguel Angel Gama Marroquin and Adrian Graumnitz
//Sources:
//Learn Selection Sort in 8 minutes: https://www.youtube.com/watch?v=EwjnF7rFLns
//Learn Merge Sort in 13 minutes: https://www.youtube.com/watch?v=3j0SWDX4AtU

//Selection sort

//1a)
/**
  * Functional implementation of the selection sort.
  *
  * @param unsorted Takes a list
  * @return a sorted list
  */
def selectionSort(unsorted: List[Int]): List[Int] =
    unsorted match
        case Nil => Nil
        case _ => unsorted.min::selectionSort(unsorted.filterNot(_ == unsorted.min))


//1b)
/**
  * Functional implementation of the mergesort.
  *
  * @param unsorted Takes a list
  * @return a sorted List
  */
def mergeSort(unsorted: List[Int]): List[Int] =
    unsorted match
        case Nil => Nil
        case head::Nil => List(head)
        case _ =>
            val (left,right) = unsorted.splitAt(unsorted.length/2)
            merge(mergeSort(left), mergeSort(right))

/**
  * takes Element of the unsorted list and merges them.
  *
  * @param left Part of the list
  * @param right Part of the list
  * @return sorted elements
  */
def merge(left: List[Int], right: List[Int]) : List[Int] =
    (left, right) match
        case (Nil,_) => right
        case (_,Nil) => left
        case (headLeft::tailLeft, headRight::tailRight) =>
            if (headLeft < headRight) headLeft::merge(tailLeft,right )
            else headRight::merge(left, tailRight)


//2a)
/**
  * Recursively checks if a given list of elements is sorted.
  *
  * @param unsorted The list of elements to be checked.
  * @param counter1 A counter that keeps track of elements that are in order.
  * @param counter2 A counter that tracks elements that are out of order.
  * @return
  */
def checkSorted[A:Ordering](unsorted: List[A], counter1: Int = 0, counter2: Int = 0): String =
    val ord = summon[Ordering[A]]
    import Ordering.*
    unsorted match
        case Nil => "List is empty"
        case head::Nil => if (counter1 == 0 || counter2 == 0) "List is sorted"
                    else "List is not sorted"
        case head::tail =>
            if (ord.lt(head, tail.head)) checkSorted(tail, counter1 + 1, counter2)
            else checkSorted(tail, counter1, counter2 + 1)


//2b)
/**
  * Sums all elements in the list that are smaller than the given value.
  *
  * @param sumList List of Elements
  * @param value The value to compare each element of the list against
  * @return
  */
def sumSmaller[A: Numeric](sumList: List[A], value: A): A =
    val num = summon[Numeric[A]]
    import num.*
    (sumList.filter(_<value)).sum


//3a)
/**
  * Represents a boolean expression with logical operations.
  * This enum defines various types of boolean expressions
  */
enum Bool:
    case True
    case False
    case And(left: Bool, right: Bool)
    case Or(left: Bool, right: Bool)
    case Not(inner: Bool)


//3b)
/**
  * Evaluates a given boolean expression represented by the `Bool` enum.
  *
  * @param expr Takes an boolean expression
  * @return
  */
def eval(expr: Bool): Boolean =
    expr match
        case Bool.True => true
        case Bool.False => false
        case Bool.And(left,right) => eval(left) && eval(right)
        case Bool.Or(left,right) => eval(left) || eval(right)
        case Bool.Not(inner) => !eval(inner)


//3c)
/**
  * Recursively negates the boolean values in a boolean expression without changing its structure.
  *
  * @param expr
  * @return
  */
def negateVals(expr: Bool): Bool = 
    expr match
        case Bool.True => Bool.False  
        case Bool.False => Bool.True   
        case Bool.And(left, right) => Bool.And(negateVals(left), negateVals(right)) 
        case Bool.Or(left, right) =>  Bool.Or(negateVals(left), negateVals(right))  
        case Bool.Not(inner) =>  Bool.Not(negateVals(inner))   

@main
def main(): Unit =
    var unsorted = List(1,3,2,5,4,8,7,6)
    var unsorted2 = List(9,8,7)
    //1a)
    println(selectionSort(unsorted2))
    //1b)
    println(mergeSort(unsorted))

    //2a)
    println(checkSorted(List(1,3,99,1083, 1082)))
    //2b)
    println(sumSmaller(unsorted2,9))

    //3a) and b)
    val bool: Bool = Bool.Not(Bool.And(Bool.True,Bool.False))
    val bool2: Bool = Bool.Or(Bool.False, Bool.True)
    println(eval(bool))
    println(eval(bool2))
    //3c)
    println(negateVals(Bool.Not(Bool.And(Bool.False,Bool.False))))
