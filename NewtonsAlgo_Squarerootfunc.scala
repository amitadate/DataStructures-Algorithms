object NewtonAlgo{
  def iterate(guess:Double, x:Double):Double=
    if(isGoodEnough(guess,x)) guess else
      iterate(improve(guess,x),x)

  def isGoodEnough(guess:Double, x:Double):Boolean=
    abs((guess*guess)-x)/x<0.001

  def improve(guess:Double, x:Double):Double=
    (guess+x/guess)/2

  def abs(v:Double):Double=if(v>0) v else -v

  def sqrt(x:Double):Double=iterate(1.0,x)

  sqrt(9)

  sqrt(1e60)
}
