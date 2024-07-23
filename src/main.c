// file: main.c

#include "mul_fortran.h"
#include <stdio.h>

int main( void ) {
	int x = 4;
	int y = 5;
	int res;

	// Compute the product, passing arguments by reference:
	mul( &x, &y, &res );

	printf( "The product of %d and %d is %d\n", x, y, res );
	return 0;
}
