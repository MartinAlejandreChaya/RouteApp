

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
        traffic_str = route["traffic"]["duration"]["text"]

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

    const div_importante = document.createElement("div");
    const pp1= document.createElement("p");
    pp1.innerHTML = "Dificultad: <b>" + route["route_data"]["dificultad_tecnica"] + "</b>";
    const pp2 = document.createElement("p");
    pp2.innerHTML = "Distancia: <b>" + route["route_data"]["distancia"] + "</b>";
    const pp3 = document.createElement("p");
    pp3.innerHTML = "Tipo de ruta: <b>" + route["route_data"]["tipo_ruta"] + "</b>";
    const pp8 = document.createElement("p");
    pp8.innerHTML = "Trailrank: <b>" + route["route_data"]["trailrank"] + "</b>";
    

    const div_1 = document.createElement("div");
    const pp4 = document.createElement("p");
    pp4.innerHTML = "Altitud máxima: <b>" + route["route_data"]["altitud_maxima"] + "</b>";
    const pp5 = document.createElement("p");
    pp5.innerHTML = "Altitud mínima: <b>" + route["route_data"]["altitud_minima"] + "</b>";
    
    const div_2 = document.createElement("div");
    const pp6 = document.createElement("p");
    pp6.innerHTML = "Desnivel negativo: <b>" + route["route_data"]["desnivel_negativo"] + "</b>";
    const pp7 = document.createElement("p");
    pp7.innerHTML = "Desnivel positivo: <b>" + route["route_data"]["desnivel_positivo"] + "</b>";
    
    
    const pp9 = document.createElement("p");
    pp9.innerHTML = "Página de descarga: <a href=" + route["route_data"]["pagina_descarga"] + " target='_blank'>" + "Link de descarga" + "</a>";

    
    div_importante.appendChild(pp1);
    div_importante.appendChild(pp2);
    div_importante.appendChild(pp3);
    div_importante.appendChild(pp8);
    rest_div.appendChild(div_importante);

    
    div_1.appendChild(pp4);
    div_1.appendChild(pp5);
    rest_div.appendChild(div_1);

    div_2.appendChild(pp6);
    div_2.appendChild(pp7);
    rest_div.appendChild(div_2);

    
    rest_div.appendChild(pp9);

    if (route["route_data"]["estrellas"]){
        const pp0 = document.createElement("p");
        pp0.innerHTML = "Estrellas: <b>" + route["route_data"]["estrellas"] + "</b>";
        rest_div.appendChild(pp0);
    }
    if (route["alojamientos"]){
        const pp10 = document.createElement("p");
        pp20.innerHTML = "Estrellas: <b>" + route["route_data"]["estrellas"] + "</b>";
        rest_div.appendChild(pp10);
    }
    if (route["clima"]){
        const pp20 = document.createElement("p");
        pp20.innerHTML = "Estrellas: <b>" + route["route_data"]["estrellas"] + "</b>";
        rest_div.appendChild(pp20);
    }

    const div_3 = document.createElement("div");
    const pp31 = document.createElement("p");
    pp31.innerHTML = "Distancia a inicio: <b>" + route["traffic"]["distance"]["text"] + "</b>";
    const pp32 = document.createElement("p");
    pp32.innerHTML = "Duración del viaje hasta inicio: <b>" + route["traffic"]["duration"]["text"] + "</b>";
    //const pp33 = document.createElement("p");
    //pp7.innerHTML = "Desnivel positivo: <b>" + route["traffic"]["duration_in_traffic"] + "</b>";

    div_3.appendChild(pp31);
    div_3.appendChild(pp32);
    //div_3.appendChild(pp33);
    rest_div.appendChild(div_3);


    cont.appendChild(title_div);
    cont.appendChild(rest_div);
}