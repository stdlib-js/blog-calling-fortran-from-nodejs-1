! file: mul.f90

!>
! Multiplies two integer values.
!
! @param {integer} x - first input value
! @param {integer} y - second input value
! @param {integer} res - output argument for storing the result
!<
subroutine mul( x, y, res )
    integer, intent(in) :: x, y
    integer, intent(out) :: res
    res = x * y
end subroutine mul
