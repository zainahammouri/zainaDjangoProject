// sweet alert
function Message(){
    Swal.fire({
        title: 'Hello,',
        text: 'There are the most skilled doctors on this site. You can now book your appointment with the doctor you want',
        imageUrl:  "{% static '/image/WelcomeImage.jpg' %} ",
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Custom image',
      })
}
const h1=document.querySelector('#open');
h1.addEventListener('open',Message());