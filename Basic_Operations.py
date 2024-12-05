#
#
#This is a script that calculates the sum, average and sum of cubes of 3 numbers stored in the variables a, b, c
#
#

A = float( input( "\nEnter the number A: " ) )

B = float( input( "\nEnter the number B: " ) )

C = float( input( "\nEnter the number C: " ) )

#Display the numbers

print( "\nThe numbers are:\n" )
print( "  Number A = ", A )
print( "  Number B = ", B )
print( "  Number C = ", C )


tot = (A+B+C)
average= ((A+B+C)/3)
sum_of_cubes= (A**2+B**2+C**2)

# Output the results

print( "The sum is", tot) 
print( "The average is", average)
print("The sum of cubes is", sum_of_cubes)