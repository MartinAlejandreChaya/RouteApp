

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
    else
        alojamiento_str = route["alojamientos"]["min_price"]
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
    
    right_div.appendChild(createText("Cómo llegar:"));
    right_div.appendChild(map);

    title_div.appendChild(left_div);
    title_div.appendChild(right_div);

    title_div.classList.add("route_header");
    right_div.classList.add("right_div");
    

    const rest_div = document.createElement("div");
    rest_div.classList.add("route_rest")
    // Four sections
    const route_div = document.createElement("div");
    const traffic_div = document.createElement("div");
    const climate_div = document.createElement("div");
    const aloj_div = document.createElement("div");

    // Ruta
    route_div.appendChild(createBigText("Información ruta"));
    route_div.appendChild(createText("Estrellas <b>" + route["route_data"]["estrellas"] + "</b>"));
    route_div.appendChild(createText("Desnivel: positivo <b>" + 
        route["route_data"]["desnivel_positivo"]  + "</b>. negativo <b>" + 
        route["route_data"]["desnivel_negativo"] + "</b>"));
    route_div.appendChild(createText("Link ruta <a target=\"_blank\" href=\"" + route["route_data"]["pagina_descarga"] + "\">Link</a>"));

    // Clima
    climate_div.appendChild(createBigText("Información clima"));
    climate_div.appendChild(createText("Temperatura: mínima <b>" + 
        route["clima"]["Temperatura"]["Minima"] + "</b> máxima <b>" +
        route["clima"]["Temperatura"]["Maxima"] + "</b>"));
    climate_div.appendChild(createText("Precipitación: <b>" + route["clima"]["Precipitacion"] + "%"));

    // Tráfico
    traffic_div.appendChild(createBigText("Información tráfico"));

    // Alojamiento
    aloj_div.appendChild(createBigText("Información alojamiento"));

    rest_div.appendChild(route_div);
    rest_div.appendChild(traffic_div);
    rest_div.appendChild(climate_div);
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