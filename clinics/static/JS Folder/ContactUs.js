// function for sweet alert:
function Alert(){
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'Your Answer has been saved',
        showConfirmButton: false,
        timer: 3000
      })
}
const s=document.querySelector('#sb');
s.addEventListener("submit",Alert());
