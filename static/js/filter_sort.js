
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
