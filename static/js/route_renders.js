

// ROUTE LIST ITEM
function createRouteLi(route) {
    const li = document.createElement("li");

    // Title
    const title_div = document.createElement("div");

    const h3 = document.createElement("h3");
    h3.innerHTML = route["titulo"];

    title_div.appendChild(h3);
    title_div.classList.add("route_title_div");

    // Rest
    const rest_div = document.createElement("div");

    // First  level
    const lev_1 = document.createElement("div");

    const p1 = document.createElement("p");
    p1.innerHTML = "Dificultad: <b>" + route["dificultad"] + "</b>";
    const p2 = document.createElement("p");
    p2.innerHTML = "Longitud: <b>" + route["longitud"] + "</b>";

    lev_1.appendChild(p1);
    lev_1.appendChild(p2);

    // Third level
    const lev_2 = document.createElement("div");

    const p3 = document.createElement("p");
    p3.innerHTML = "Clima: <b>" + route["clima"] + "</b>";
    const p4 = document.createElement("p");
    p4.innerHTML = "Transporte: <b>" + route["tiempo_transporte"] + "</b>";

    lev_2.appendChild(p3);
    lev_2.appendChild(p4);


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
    h2.innerHTML = route["titulo"];

    title_div.appendChild(h2);


    // REST
    const rest_div = document.createElement("div");

    const p = document.createElement("p");
    p.innerHTML = "Aquí iría el resto de información relevante sobre la ruta (mapas, punto de partida, hoteles...)"

    rest_div.appendChild(p);


    cont.appendChild(title_div);
    cont.appendChild(rest_div);
}