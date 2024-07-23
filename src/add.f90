! file: add.f90

!>
! Adds two integer values.
!
! @param {integer} x - first input value
! @param {integer} y - second input value
!<
integer function add( x, y )
    ! Define the input parameters:
    integer, intent(in) :: x, y
    ! ..
    ! Compute the sum:
    add = x + y
end function add

!>
! Main execution sequence.
!<
program main
    ! Local variables:
    character(len=999) :: str, tmp
    ! ..
    ! Intrinsic functions:
    intrinsic adjustl, trim
    ! ..
    ! Define a variable for storing the sum:
    integer :: res
    ! ..
    ! Compute the sum:
    res = add( 12, 15 )
    ! ..
    ! Print the results:
    write (str, '(I15)') res
    tmp = adjustl( str )
    print '(A, A)', 'The sum of 12 and 15 is ', trim( tmp )
end program
