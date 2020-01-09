! This is the main program for the model

program main

    use params
    use model_vars
    
    implicit none
    
    integer :: i
    integer :: nnt
    ! Iterating variable
    
    print *, "Loaded Parameters and Variables ..."
    
    call init
    print *, "Data initialized! Starting Calculations! ..."
    
    do i = 2, nt
    
        call rk4(i-1)
        print *, "Calculations done for timestep t = ",i-1, " of ", nt-1

    end do
    
!    nnt=nt/100
!    do i =2,nnt
!        call data_saver2(100*(i-1)) 
!    end do

    print *, "All Calculations done! Saving data! ..."
    call data_saver
    print *, "All data saved successfully! Exiting ..."

end program main
