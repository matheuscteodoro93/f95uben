! saving snapshots (one by one) implitic none

subroutine data_saver2(tsnap)

    use params
    use model_vars

    implicit none

    integer, intent(in) :: tsnap
    character(len=150)  :: filepath,filename
    integer             :: ios,i,j

    filepath="output/"

    write(filename,"(I4)") tsnap

    write(*,*) "saving data at", TRIM(ADJUSTL(filepath))//TRIM(ADJUSTL(filename))

    open(42,file=TRIM(ADJUSTL(filepath))//TRIM(ADJUSTL(filename)) &
     ,status='new',iostat=ios)
    
    do i=1,nx
      do j=1,ny

        write(42,*) xx(i,j), yy(i,j), h(i,j,tsnap) 

      enddo
    enddo

    if(ios.ne.0) then
     print*, "problem opening the file"
    endif

    close(42)

end subroutine data_saver2

