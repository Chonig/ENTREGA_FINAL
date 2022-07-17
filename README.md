# entrega_final

# este proyecto esta dedicado para cumplir los puntos en la Entrega Parcial del Proyecto Final de CoderHouse #

# se siguieron los paso similares a lo visto en clase
# se generaron vistas , las cuales generan interacción entre el usuario y el servidor
# tanto con el fomulario web, como con la solicitud de contacto, se logran persistir los datos en la BD del PROYECYO_FINAL
# para los las vistas "html", se generaron stilos staticos, con el editor css
# se crearon 4 modelos ( Persona, Datos, Articulos, Contacto)
# se crearon 3 formularios (FormularioReserva,BusquedaPersona,FormularioContacto)

 # para el cuerpo -------------->"
 
    body{
    font-family: arial, helvetica;
    background: #979595;
    text-align: center;
}
# para el menu de navegación----------->#
.menu{
    list-style: none ;
    padding: 0;
    background: #092327;
    width: 90%;
    max-width: 1000px;
    margin: auto;
}

.menu li a{
    text-decoration: none;
    color: white;
    padding: 20px;
    display: block;

}

.menu li{
    display: inline-block;
    text-align: center;

}

.menu li a:hover{
    background: #ef8354;
}



# para el pie de pagina --------------->
footer{
    max-width: 1000px;
    padding: 30px;
    background: #092327;
    margin: auto;
    border-radius: 0 0 20px 20px;
    color: white;
    text-align: center;
    box-sizing: border-box;
    font-family: Arial, Helvetica;
    font-size: 18px;
}

footer a:hover{
    color: rgb(242, 241, 240);
    background: #ef8354;
}

# y tambien para el cuerpo de los formularios y las debas paginas dentro de la navegación------->
.container{
    height: 50vh;
    margin: 5%;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;


}