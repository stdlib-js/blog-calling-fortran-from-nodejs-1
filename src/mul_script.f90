! file: mul_script.f90

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
    ! Define a variable for storing the product:
    integer :: res
    ! ..
    ! Call the `mul` subroutine to compute the product:
    call mul( 4, 5, res )
    ! ..
    ! Print the results:
    write (str, '(I15)') res
    tmp = adjustl( str )
    print '(A, A)', 'The product of 4 and 5 is ', trim( tmp )
end program
