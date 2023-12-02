
let sort_options_displayed = false;
let filter_options_displayed = false;

let order_select_value = "ascendente";
let order_crit_value = "recomendado"

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
                }
            });
        });
    });
    const order_select = document.getElementById("order_crit_select");
    order_crit_select.addEventListener("change", () => {
        order_select_value = order_crit_select.value;
        routes = reorder_routes(routes);
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
            default:
                console.log("ERROR: No order criterion", order_crit_value);
                break;
        }
        if (order_select_value == "ascendente")
            return diff;
        else
            return -diff;
    });
    show_routes(routes)
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


// FILTRAR
function toggleRange(toggleCheckbox, slider_id) {
    var slider = document.getElementById(slider_id);
    slider.disabled = !toggleCheckbox.checked;

    prop = slider.name.split("_")[0]
    prop_span = document.getElementById("filter_" + prop + "_span");
    dict = get_filter_dict(prop)

    filter_change(prop, prop_span, dict, slider.value)

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

function filter_change(property, span, dict, value) {
    span.innerHTML = dict[value];
    // TODO: Actually filter
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
    0: "Muy fácil",
    25: "Fácil",
    50: "Moderado",
    75: "Difícil",
    100: "Muy difícil"
}

distancia_filter_dict = {
    0: "0km - 5km",
    25: "5km - 10km",
    50: "10km - 20km",
    75: "20km - 40km",
    100: ">40 km"
}

transporte_filter_dict = {
    0: "< 20m",
    25: "< 40m",
    50: "< 1h",
    75: "< 2h",
    100: "> 2h"
}