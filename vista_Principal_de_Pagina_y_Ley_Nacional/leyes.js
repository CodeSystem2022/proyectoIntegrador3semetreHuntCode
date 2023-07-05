$(document).ready(function() {
  // Agregar controlador de evento para el envío del formulario
  $("#searchForm").submit(function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    var searchTerm = $("#searchInput").val(); // Obtener el término de búsqueda
    var selectedCategory = $(".button-group button.active").data("category"); // Obtener la categoría seleccionada

    switch (selectedCategory) {
      case "leyes":
        buscarEnLeyes(searchTerm);
        break;
      case "decretos":
        buscarEnDecretos(searchTerm);
        break;
      case "resoluciones":
        buscarEnResoluciones(searchTerm);
        break;
      case "recursos":
        buscarEnRecursos(searchTerm);
        break;
      case "misfavoritos":
        buscarEnMisFavoritos(searchTerm);
        break;
      case "masvisitados":
        buscarEnMasVisitados(searchTerm);
        break;
      default:
        buscar(searchTerm);
    }
  });

  // Agregar controladores de evento para los botones de búsqueda
  $(".button-group button").click(function() {
    $(".button-group button").removeClass("active");
    $(this).addClass("active");
  });

  // Agregar controlador de evento para el ícono de búsqueda
  $(".icon").click(function() {
    $("#searchForm").submit();
  });

  // Funciones de búsqueda
  function buscarEnLeyes(searchTerm) {
    console.log("Realizando búsqueda en la categoría 'leyes' con el término: " + searchTerm);
    // Lógica de búsqueda específica para la categoría 'leyes'
  }

  function buscarEnDecretos(searchTerm) {
    console.log("Realizando búsqueda en la categoría 'decretos' con el término: " + searchTerm);
    // Lógica de búsqueda específica para la categoría 'decretos'
  }

  function buscarEnResoluciones(searchTerm) {
    console.log("Realizando búsqueda en la categoría 'resoluciones' con el término: " + searchTerm);
    // Lógica de búsqueda específica para la categoría 'resoluciones'
  }

  function buscarEnRecursos(searchTerm) {
    console.log("Realizando búsqueda en la categoría 'recursos' con el término: " + searchTerm);
    // Lógica de búsqueda específica para la categoría 'recursos'
  }

  function buscarEnMisFavoritos(searchTerm) {
    console.log("Realizando búsqueda en la categoría 'mis favoritos' con el término: " + searchTerm);
    // Lógica de búsqueda específica para la categoría 'mis favoritos'
  }

  function buscarEnMasVisitados(searchTerm) {
    console.log("Realizando búsqueda en la categoría 'más visitados' con el término: " + searchTerm);
    // Lógica de búsqueda específica para la categoría 'más visitados'
  }

  function buscar(searchTerm) {
    console.log("Realizando búsqueda general con el término: " + searchTerm);
    // Lógica de búsqueda general
  }
});



document.getElementById("leyesBtn").addEventListener("click", function() {
  // Acciones a realizar cuando se hace clic en el botón "LEYES"
  console.log("Se hizo clic en el botón LEYES");
});
document.getElementById("decretosBtn").addEventListener("click", function() {
    // Acciones a realizar cuando se hace clic en el botón "DECRETOS"
    console.log("Se hizo clic en el botón DECRETOS");
});

document.getElementById("resolucionesBtn").addEventListener("click", function() {
    // Acciones a realizar cuando se hace clic en el botón "RESOLUCIONES"
    console.log("Se hizo clic en el botón RESOLUCIONES");
});

document.getElementById("recursosBtn").addEventListener("click", function() {
   
    console.log("Se hizo clic en el botón RECURSOS");
});
  
document.getElementById("misfavoritosBtn").addEventListener("click", function() {
   
    console.log("Se hizo clic en el botón MIS FAVORITOS");
});

document.getElementById("masvisitadosBtn").addEventListener("click", function() {
    
    console.log("Se hizo clic en el botón MAS VISITADOS");
});
