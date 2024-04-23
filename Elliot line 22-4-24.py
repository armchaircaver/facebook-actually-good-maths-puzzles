"""
puzzle on facebook group "actually good maths puzzles"
https://www.facebook.com/groups/1923323131245618/permalink/3966411526936758/
"""

from math import floor,pi

def calculate_ratio():
  chordsum = 1.0
  k=1 

  pi_over_4 = pi/4.0
  sqrt3 = 3**0.5

  while 1:
    x = 2*k
    # find even integer m :  m < sqrt(3)*x < m+2
    m = int( sqrt3*x )
    if m%2: m -= 1

    # chord length for circle centred at (x,m)
    d = ( sqrt3*x - m)/2.0
    chord1 = 2*(1.0 - d*d)**0.5

    # chord length for circle centred at (x,m+2)
    d -= 1.0
    chord2 = 2*(1.0 - d*d)**0.5

    chordsum += chord1
    chordsum += chord2


    if k%5000000==0:
      hypotenuse = 2*(x+1)
      ratio = chordsum/hypotenuse
      print(k, ratio, ratio - pi_over_4)
      

    k+=1


calculate_ratio()  
"""
results

5000000 0.7853981535255428 -9.871905515268509e-09
10000000 0.7853981641871385 7.896902021187202e-10
15000000 0.785398162391602 -1.0058462951434421e-09
20000000 0.7853981641557735 7.583251804277324e-10
25000000 0.7853981629745937 -4.2285452916956956e-10
30000000 0.7853981652548496 1.8574013438410475e-09
35000000 0.7853981667885117 3.3910634300582387e-09
40000000 0.7853981657742892 2.3768409462832096e-09
45000000 0.7853981659938603 2.596411974309376e-09
50000000 0.7853981645930467 1.1955983980627138e-09
55000000 0.7853981644043033 1.0068550437836166e-09
60000000 0.7853981634309839 3.3535618726432403e-11
65000000 0.7853981638624132 4.6496495542669436e-10
70000000 0.785398164383417 9.859687510882509e-10
75000000 0.7853981638820041 4.845558398969274e-10
80000000 0.7853981639845967 5.871484409780692e-10
85000000 0.7853981631103603 -2.8708802002341827e-10
90000000 0.7853981632841995 -1.1324874371609894e-10
95000000 0.7853981626856247 -7.118236000636102e-10
100000000 0.7853981630783453 -3.191029662730216e-10
105000000 0.7853981633098549 -8.759337699615344e-11
110000000 0.7853981631242984 -2.731498360830642e-10
115000000 0.7853981629921353 -4.053130053804921e-10
120000000 0.7853981626253969 -7.720514227926856e-10
125000000 0.7853981627807529 -6.166953614439308e-10
130000000 0.785398162506079 -8.913693116952004e-10
"""  
                                          
