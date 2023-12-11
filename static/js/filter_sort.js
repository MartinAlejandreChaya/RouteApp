
let sort_options_displayed = false;
let filter_options_displayed = false;

let order_select_value = "ascendente";
let order_crit_value = "recomendado"

let filter_crit_dificultad = false;
let filter_crit_transporte = false;
let filter_crit_distancia = false;
let distancia_lims = [];
let transporte_lims = [];
let dificultad_lims = "";

function setup_sort_filter() {
    const filter_li = document.getElementById("filter_li");
    const sort_li = document.getElementById("sort_li");

    sort_li.addEventListener("click", (event) => {
        const sort_div = document.getElementById("sort_options")
        if (sort_options_displayed) {
            sort_div.style.height = "0px"
            sort_div.style.padding = "0px 10px"
            sort_div.style.margin = "0px"
        }
        else {
            sort_div.style.height = sort_div.scrollHeight + 'px';
            sort_div.style.padding = "5px 10px"
            sort_div.style.margin = "5px 0"
        }
        sort_options_displayed = !sort_options_displayed;
    })

    const checkboxes = document.querySelectorAll('.checkboxes');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            checkboxes.forEach(cb => {
                if (cb !== this) {
                    cb.checked = false;
                }
                else {
                    order_crit_value = cb.value;
                    routes = reorder_routes(routes);
                    show_routes(routes);
                }
            });
        });
    });
    const order_select = document.getElementById("order_crit_select");
    order_select.addEventListener("change", () => {
        order_select_value = order_select.value;
        routes = reorder_routes(routes);
        show_routes(routes);
    })

    filter_li.addEventListener("click", (event) => {
        const filter_div = document.getElementById("filter_options")
        if (filter_options_displayed) {
            filter_div.style.height = "0px"
            filter_div.style.padding = "0px 10px"
            filter_div.style.margin = "0px"
        }
        else {
            filter_div.style.height = filter_div.scrollHeight + 'px';
            filter_div.style.padding = "5px 10px"
            filter_div.style.margin = "5px 0"
        }
        filter_options_displayed = !filter_options_displayed;
    })


    setup_filter_values();
}

function reorder_routes(routes) {
    console.log("Reordering for", order_select_value, order_crit_value)
    routes = routes.sort((a, b) => {
        let diff = 0;
        switch (order_crit_value) {
            case "dificultad":
                diff = get_dict_val(dificultad_dict, a["route_data"]["dificultad_tecnica"]) -
                    get_dict_val(dificultad_dict, b["route_data"]["dificultad_tecnica"]);
                break;
            case "distancia":
                a_dist = parseFloat(a["route_data"]["distancia"].split(" ")[0].replace(',', '.'))
                b_dist = parseFloat(b["route_data"]["distancia"].split(" ")[0].replace(',', '.'))
                diff = a_dist - b_dist;
                break;
            case "transporte":
                diff = a["traffic"]["duration_in_traffic"]["value"] - b["traffic"]["duration_in_traffic"]["value"]
                break;
            case "alojamiento":
                diff = a["alojamientos"]["min_price"]["value"] - b["alojamientos"]["min_price"]["value"];
                break;
            default:
                console.log("ERROR: No order criterion", order_crit_value);
                break;
        }
        if (order_select_value == "ascendente")
            return diff;
        else
            return -diff;
    });
    return routes;
}

dificultad_dict = {
    "Fácil": 0,
    "Moderado": 1,
    "Difícil": 2,
    "Muy difícil": 3
}
function get_dict_val(dict, val) {
    if (val in dict)
        return dict[val]
    else {
        console.log("Value " + val + " not in dificultad_dict: ", dict)
        return 0;
    }
}


function filter_routes(routes) {
    filtered_routes = routes;

    filtered_routes.forEach((route) => {
        filtered = false;
        if (filter_crit_dificultad)
            filtered = filtered || route["route_data"]["dificultad_tecnica"] != dificultad_lims;
        if (filter_crit_distancia) {
            let dist = parseFloat(route["route_data"]["distancia"].split(" ")[0].replace(",", "."))
            filtered = filtered || dist < distancia_lims[0] || dist > distancia_lims[1]
        }
            
        if (filter_crit_transporte)
            filtered = filtered || filter_transport_time(route["traffic"]["duration_in_traffic"])
        route["filtered"] = filtered;
    })

    return filtered_routes;
}


// FILTRAR
function toggleRange(toggleCheckbox, slider_id) {
    var slider = document.getElementById(slider_id);
    slider.disabled = !toggleCheckbox.checked;

    prop = slider.name.split("_")[0]
    prop_span = document.getElementById("filter_" + prop + "_span");
    dict = get_filter_dict(prop)

    filter_change(prop, prop_span, dict, slider.value, disable=slider.disabled)

    if (slider.disabled) {
        prop_span.innerHTML = "";
    }
}


function setup_filter_values() {
    dificultad_range = document.getElementById("dificultad_range");
    dificultad_span = document.getElementById("filter_dificultad_span");

    dificultad_range.addEventListener("input", () => {
        filter_change("dificultad", dificultad_span, dificultad_filter_dict, dificultad_range.value)
    })


    distancia_range = document.getElementById("distancia_range");
    distancia_span = document.getElementById("filter_distancia_span");

    distancia_range.addEventListener("input", () => {
        filter_change("distancia", distancia_span, distancia_filter_dict, distancia_range.value)
    })


    transporte_range = document.getElementById("transporte_range");
    transporte_span = document.getElementById("filter_transporte_span");

    transporte_range.addEventListener("input", () => {
        filter_change("transporte", transporte_span, transporte_filter_dict, transporte_range.value)
    })

}

function filter_change(property, span, dict, value, disable=false) {
    span.innerHTML = dict[value][0];

    if (property == "dificultad") {
        filter_crit_dificultad = !disable;
        dificultad_lims = dict[value][1];
    }
    else if (property == "distancia") {
        filter_crit_distancia = !disable;
        distancia_lims = dict[value][1]
    }
    else if (property == "transporte") {
        filter_crit_transporte = !disable;
        transporte_lims = dict[value][1]
    }

    routes = filter_routes(routes);
    show_routes(routes);
}

function get_filter_dict(prop) {
    if (prop == "dificultad")
        return dificultad_filter_dict
    else if (prop == "distancia")
        return distancia_filter_dict
    else if (prop == "transporte")
        return transporte_filter_dict
    else {
        console.log("Error: No filter property: " + prop);
        return {}
    }
}

dificultad_filter_dict = {
    0: ["Muy fácil", "Muy fácil"],
    25: ["Fácil", "Fácil"],
    50: ["Moderado", "Moderado"],
    75: ["Difícil", "Difícil"],
    100: ["Muy difícil", "Muy difícil"]
}

distancia_filter_dict = {
    0: ["0km - 5km", [0, 5]],
    25: ["5km - 10km", [5, 10]],
    50: ["10km - 20km", [10, 20]],
    75: ["20km - 40km", [20, 40]],
    100: ["> 40 km", [40, 1000000000]]
}

transporte_filter_dict = {
    0: ["< 20m", [0, 20]],
    25: ["< 40m", [0, 40]],
    50: ["< 1h", [0, 60]],
    75: ["< 2h", [0, 120]],
    100: ["> 2h", [120, 1000000000]]
}

function filter_transport_time(time) {
    return time["value"] < transporte_lims[0]*60 || time["value"] > transporte_lims[1]*60
}