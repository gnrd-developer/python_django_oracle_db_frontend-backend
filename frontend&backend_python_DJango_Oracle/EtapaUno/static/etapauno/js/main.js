const btn = document.querySelector('#btn');

const configUser = window.matchMedia('(prefers-color-scheme: dark)');

const localConfig = localStorage.getItem('tema');
if(localConfig === 'dark'){
    document.body.classList.toggle('dark')
}else if(localConfig === 'light'){
    document.body.classList.toggle('light')
}

btn.addEventListener('click', () => {
    //console.log(configUser.matches)
    let colorTema;
    if(configUser.matches){
        document.body.classList.toggle('light')
        colorTema = document.body.classList.contains('light') ? 'light' : 'dark' //expresion ternaria o if corto
    }
    else{
        document.body.classList.toggle('dark')

        colorTema = document.body.classList.contains('dark') ? 'dark' : 'light'
    }
    localStorage.setItem('tema',colorTema)
})

function validacion()
{
    uno = document.getElementById('region').selectedIndex;
    unoa = document.getElementById('region').options;
    dos = document.getElementById('ciudad').selectedIndex;
    dosa = document.getElementById('ciudad').options;
    tres = document.getElementById('comuna').selectedIndex;
    tresa = document.getElementById('comuna').options;
    prima = document.getElementById('comentarios').value;

    if (uno == null || uno == 0)
    {
        alert('Seleccione un Región');
        return false;
    }

    if (dos == null || dos == 0)
    {
        alert('Seleccione una Ciudad');

        return false;
    }

    if (tres == null || tres == 0)
    {
        alert('Seleccione un Comuna');

        return false;
    }

    if(prima == "" || prima == null){
        alert("Hola, por favor de detalles de su post.");
        return false;
    }

    return true;

}

function validacion2()
{
    cuatro = document.getElementById('region2').selectedIndex;
    cuatroa = document.getElementById('region2').options;
    cinco = document.getElementById('ciudad2').selectedIndex;
    cincoa = document.getElementById('ciudad2').options;
    seis = document.getElementById('comuna2').selectedIndex;
    seisa = document.getElementById('comuna2').options;
    siete = document.getElementById('comentarios').value;

    if (cuatro == null || cuatro == 0)
    {
        alert('Seleccione una Región');

        return false;
    }

    if (cinco == null || cinco == 0)
    {
        alert('Seleccione un Ciudad');

        return false;
    }

    if (seis == null || seis == 0)
    {
        alert('Seleccione un Comuna');

        return false;
    }

    if(siete == "" || siete == null){
        alert("Hola, por favor de detalles de la venta");
        return false;
    }

    return true;

}

function validateForm() {
    var x = document.forms["uno"]["email"].value;
    var y = document.forms["uno"]["password"].value;
    if (x == "" || x == null) {
      alert("Hola, por favor ingrese un correo electronico");
      return false;
    }

    if (y == "" || y == null) {
        alert("Hola, por favor ingrese una clave");
        return false;
      }
  }