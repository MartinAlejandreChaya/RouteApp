

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
        clima_str = route["clima"]
    p4.innerHTML = "Clima: <b>" + clima_str + "</b>";
    // Traffic
    const p5 = document.createElement("p");
    traffic_str = "";
    if (route["traffic"] == false)
        traffic_str = route["traffic_error"]
    else
        traffic = route["traffic"]
    p5.innerHTML = "Transporte: <b>" + traffic_str + "</b>";
    // Link ruta
    const p6 = document.createElement("p")
    p6.innerHTML = "Link descarga: <a target='_blank' href=" + route["route_data"]["pagina_descarga"] + " >" + "Link ruta</a>";

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

    // TITLE
    const title_div = document.createElement("div");

    const h2 = document.createElement("h2");
    h2.innerHTML = route["route_data"]["nombre"];

    title_div.appendChild(h2);


    // REST
    const rest_div = document.createElement("div");

    const p = document.createElement("p");
    p.innerHTML = "Aquí iría el resto de información relevante sobre la ruta (mapas, punto de partida, hoteles...)"

    rest_div.appendChild(p);


    cont.appendChild(title_div);
    cont.appendChild(rest_div);
}