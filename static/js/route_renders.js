

// ROUTE LIST ITEM
function createRouteLi(route) {
    const li = document.createElement("li");

    // Title
    const title_div = document.createElement("div");

    const h3 = document.createElement("h3");
    h3.innerHTML = route["route_data"]["nombre"];

    title_div.appendChild(h3);
    title_div.classList.add("route_title_div");

    // Rest
    const rest_div = document.createElement("div");

    // First  level
    const lev_1 = document.createElement("div");

    const p1 = document.createElement("p");
    p1.innerHTML = "Dificultad: <b>" + route["route_data"]["dificultad_tecnica"] + "</b>";
    const p2 = document.createElement("p");
    p2.innerHTML = "Distancia: <b>" + route["route_data"]["distancia"] + "</b>";
    const p3 = document.createElement("p");
    p3.innerHTML = "Tipo de ruta: <b>" + route["route_data"]["tipo_ruta"] + "</b>";

    lev_1.appendChild(p1);
    lev_1.appendChild(p2);
    lev_1.appendChild(p3);

    // Third level
    const lev_2 = document.createElement("div");
    // Clima
    const p4 = document.createElement("p");
    clima_str = "";
    if (route["clima"] == false)
        clima_str = route["clima_error"]
    else
        clima_str = route["clima"]["Estado del cielo"]
    p4.innerHTML = "Clima: <b>" + clima_str + "</b>";
    // Traffic
    const p5 = document.createElement("p");
    traffic_str = "";
    if (route["traffic"] == false)
        traffic_str = route["traffic_error"]
    else
        traffic_str = route["traffic"]["duration"]["text"]

    p5.innerHTML = "Transporte: <b>" + traffic_str + "</b>";

    // Alojamiento
    const p6 = document.createElement("p")
    let alojamiento_str = ""
    if (route["alojamientos"] == false)
        alojamiento_str = route["alojamientos_error"]
    else {
        alojamiento_str = route["alojamientos"]["min_price"]["value"] +
            " " + route["alojamientos"]["min_price"]["currency"]
    }
    p6.innerHTML = "Alojamiento: <b>" + alojamiento_str + "</b>";

    lev_2.appendChild(p4);
    lev_2.appendChild(p5);
    lev_2.appendChild(p6);


    rest_div.appendChild(lev_1);
    rest_div.appendChild(lev_2);

    rest_div.classList.add("route_rest_div");

    li.appendChild(title_div);
    li.appendChild(rest_div);
    return li;
}


// ROUTE ITEM
function createRouteItem(route) {
    const cont = document.getElementById("modal_route_div");
    cont.innerHTML = "";

    const h2 = document.createElement("h2");
    h2.innerHTML = route["route_data"]["nombre"];
    cont.appendChild(h2);

    // TITLE
    const title_div = document.createElement("div");
    const map = document.createElement("iframe");
    if (route["traffic"]) {
        map.src = "https://www.google.com/maps/embed/v1/directions"
            + "?key=AIzaSyBxkPLTw1AgCBl6wkOP9wu0_xaumdy7Kcc"
            + "&origin=" + route["traffic"]["from"] 
            + "&destination=" + route["traffic"]["to"];
    }
    else {
        map.src = "https://www.google.com/maps/embed/v1/place" +
            + "?key=AIzaSyBxkPLTw1AgCBl6wkOP9wu0_xaumdy7Kcc"
            + "&q=" + route["route_data"]["punto_inicio"]["address"]
    }

    map.referrerPolicy = "no-referrer-when-downgrade";
    map.allowFullscreen = true;
    map.loading = "lazy"
    map.frameBorder = "0";
    map.style.border = "0";
    map.style.borderRadius = "5px";

    const left_div = document.createElement("div");
    const right_div = document.createElement("div");

    const div_importante = document.createElement("div");
    div_importante.appendChild(createText("Dificultad: <b>" + route["route_data"]["dificultad_tecnica"] + "</b>"));
    div_importante.appendChild(createText("Distancia: <b>" + route["route_data"]["distancia"] + "</b>"));
    div_importante.appendChild(createText("Tipo de ruta: <b>" + route["route_data"]["tipo_ruta"] + "</b>"));
    div_importante.appendChild(createText("Clima: <b>" + route["clima"]["Estado del cielo"] + "</b>"));
    div_importante.appendChild(createText("Transporte: <b>" + route["traffic"]["duration_in_traffic"]["text"] + "</b>"));
    div_importante.appendChild(createText("Alojamiento: <b>" + route["alojamientos"]["min_price"]["value"] + " " + route["alojamientos"]["min_price"]["currency"] + "</b>"));

    left_div.appendChild(div_importante);
    

    right_div.appendChild(map);

    title_div.appendChild(left_div);
    title_div.appendChild(right_div);

    title_div.classList.add("route_header");
    right_div.classList.add("right_div");
    left_div.classList.add("left_div");

    const rest_div = document.createElement("div");
    rest_div.classList.add("route_rest")
    // Four sections
    const route_div = document.createElement("div");
    const traffic_div = document.createElement("div");
    const clima_div = document.createElement("div");
    const aloj_div = document.createElement("div");

    // Ruta
    route_div.appendChild(createBigText("Ruta"));
    route_div.appendChild(createText("Estrellas <b>" + route["route_data"]["estrellas"] + "</b>"));
    route_div.appendChild(createText("Link ruta <a target=\"_blank\" href=\"" + route["route_data"]["pagina_descarga"] + "\">Link</a>"));
    const desnivelDiv = document.createElement("div");
    desnivelDiv.appendChild(createText("Altitud máxima: <b>" + route["route_data"]["altitud_maxima"]))
    desnivelDiv.appendChild(createText("Altitud máxima: <b>" + route["route_data"]["altitud_minima"]))
    desnivelDiv.appendChild(createText("Desnivel positivo: <b>" + route["route_data"]["desnivel_positivo"]))
    desnivelDiv.appendChild(createText("Desnivel negativo: <b>" + route["route_data"]["desnivel_negativo"]))
    route_div.appendChild(desnivelDiv);

    // Clima
    clima_div.appendChild(createBigText("Clima"));
    clima_div.appendChild(createText("Temperatura: <b>" +
        route["clima"]["Temperatura"]["Minima"] + "</b> - <b>" +
        route["clima"]["Temperatura"]["Maxima"] + "</b>"));
        clima_div.appendChild(createText("Sensación térmica: <b>" +
        route["clima"]["Sensacion termica"]["Minima"] + "</b> - <b>" +
        route["clima"]["Sensacion termica"]["Maxima"] + "</b>"));
    clima_div.appendChild(createText("Precipitación: <b>" + route["clima"]["Precipitacion"] + "%"));
    clima_div.appendChild(createText("Humedad relativa: " +
        route["clima"]["Humedad relativa"]["Minima"] + " - " + route["clima"]["Humedad relativa"]["Maxima"]))
    if (route["clima"]["Probabilidad de nieve"] == "") {
        clima_div.appendChild(createText("Sin probabilidad de nieve"))
    }
    else {
        clima_div.appendChild(createText("Probabilidad de nieve: <b>" +
            + route["clima"]["Probabilidad de nieve"] + "</b>. Se recomienda ropa de abrigo."))
    }
    clima_div.appendChild(createText("Velocidad del viento: " + route["clima"]["Viento"]));
    clima_div.appendChild(createText("Radiación UV: " + route["clima"]["Radiacion UV maxima"]))

    // Tráfico
    traffic_div.appendChild(createBigText("Tráfico"));
    traffic_div.appendChild(createText("Distancia <b>" + route["traffic"]["distance"]["text"] + "</b>"))
    traffic_div.appendChild(createText("Duración (sin tráfico) <b>" + route["traffic"]["duration"]["text"] + "</b>"))
    traffic_div.appendChild(createText("Duración (en tráfico) <b>" + route["traffic"]["duration_in_traffic"]["text"] + "</b>"))
    traffic_div.appendChild(createText("Desde " + route["traffic"]["from"] + "<br>Hasta " + route["traffic"]["to"]))
    const desplegable = document.createElement("ul");
    route["traffic"]["steps"].forEach((step) => {
        // Append step to desplegable
        desplegable.appendChild(createText(
            "<span class=\"traffic_distance\">" + step["distance"]["text"] + "</span> - " + step["html_instructions"]
        ))
    })
    desplegable.classList.add("listaDesplegable")
    traffic_div.appendChild(desplegable);

    // Alojamiento
    aloj_div.appendChild(createBigText("Alojamiento"));
    aloj_div.appendChild(createText("Mejor precio: <b>" + route["alojamientos"]["min_price"]["value"] + "</b>"))
    aloj_desplegable = document.createElement("ul");
    aloj_desplegable.classList.add("listaDesplegable");
    route["alojamientos"]["list"].forEach((aloj) => {
        const aloj_item = document.createElement("div");

        const aloj_title = document.createElement("div");
        aloj_title.classList.add("aloj_title_div")
        const aloj_imp = document.createElement("div");
        aloj_imp.appendChild(createText("<b>"+aloj["hotel_name"] + "</b>"))
        aloj_imp.appendChild(createText("Precio: <b>" + aloj["price_breakdown"]["all_inclusive_price"]
            + aloj["price_breakdown"]["currency"] + "</b>"))
        aloj_imp.appendChild(createText("Reseñas: <b>" + aloj["review_score"] + "</b>"))
        const hotel_img = document.createElement("img");
        hotel_img.src = aloj["main_photo_url"];
        hotel_img.classList.add("aloj_img");
        aloj_title.appendChild(aloj_imp);
        aloj_title.appendChild(hotel_img);
        aloj_item.appendChild(aloj_title)

        aloj_item.appendChild(createText("Booking <a href=\"" + aloj["url"] + "\" target=\"_blank\">link</a>"))
        aloj_item.appendChild(createText("Check-in / out: " +
            aloj["checkin"]["from"] + " - " + aloj["checkin"]["until"] + " / " +
            aloj["checkout"]["from"] + " - " + aloj["checkout"]["until"]))
        aloj_item.appendChild(document.createElement("hr"))
        aloj_desplegable.appendChild(aloj_item);
    })
    aloj_div.appendChild(aloj_desplegable);

    rest_div.appendChild(route_div);
    rest_div.appendChild(clima_div);
    rest_div.appendChild(traffic_div);
    rest_div.appendChild(aloj_div);

    cont.appendChild(title_div);
    cont.appendChild(rest_div);
}

function createText(str) {
    const p = document.createElement("p");
    p.innerHTML = str;
    return p;
}

function createBigText(str) {
    const h3 = document.createElement("h3");
    h3.innerHTML = str;
    return h3;
}