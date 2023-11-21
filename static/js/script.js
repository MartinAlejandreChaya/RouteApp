const SEARCH_INPUT_EXAMPLES = [
    "Sierra Nevada", "Pirineos", "Navacerrada"
]

let waiting_for_response = false;

// MODAL
let modal;
let cerrar_modal;

window.onload = () => {
     // Modal
    modal = document.getElementById("ventanaModal");
    cerrar_modal = document.getElementById("cerrar")
    cerrar_modal.addEventListener("click", (event) => {
        modal.style.display = "none";
    })

    // Date
    const date_input = document.getElementById("date_input");
    date_input.valueAsDate = new Date();

    // Location
    const location_input = document.getElementById("location_input");
    let location_coords = false;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            location_input.placeholder = "Localized!";
            location_coords = {
                "lat": position.coords.latitude,
                "long": position.coords.longitude
            }
        }, (err) => {
            location_input.placeholder = "Introduce location";
        });
    }
    else {
        location_input.placeholder = "Introduce location";
    }


    // Listen to search event
    const search_input = document.getElementById("search_input");
    search_input.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            if (waiting_for_response) {
                alert("Ya se está procesando una solicitud");
                return;
            }

            // PARAMS
            let req_data = {"search_title": search_input.value};
            if (search_input.value == "") {
                alert("Introduce algo en la barra de busquedas");
                return;
            }
            req_data["route_date"] = date_input.value;
            if (location_input.value == "") {
                if (location_coords) {
                    req_data["from_loc"] = {
                        "geolocated": true,
                        "location_coords": location_coords
                    };
                }
            }
            else {
                req_data["from_loc"] = {
                    "geolocated": false,
                    "location_title": location_input.value
                }
            }

            console.log("Sending GET request for data: ", req_data)
            waiting_for_response = true;
            loading_routes();
            fetch("/search_routes", {
                "method": "POST",
                "headers": {"Content-Type": "application/json"},
                "body": JSON.stringify(req_data),
            }).then( response => response.json() ).then(data => {
                console.log("Response recieved", data);
                waiting_for_response = false;

                if (data.success) {
                    show_routes(data.routes);
                }
                else {
                    show_error(data.error_msg);
                }
            });
        }
    });

    animate_placeholder_input(search_input, SEARCH_INPUT_EXAMPLES);
}

window.addEventListener("click", function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});


// Animate input function
function animate_placeholder_input(input, examples) {

    let char = 0;
    let word = examples[Math.trunc(Math.random() * examples.length)]
    let word_len = word.length;
    let sense = 1;
    let wait_frames = 0;

    setInterval(() => {
        if (char > word_len || char < 0) {
            if (wait_frames < 5) wait_frames++;
            else {
                wait_frames = 0;
                if (sense == -1) {
                    word = examples[Math.trunc(Math.random() * examples.length)]
                    word_len = word.length;
                }
                sense *= -1;
                char += sense;
            }
        }
        else {
            input.placeholder = word.substring(0, char);
            char += sense;
        }
    }, 50);
}


function loading_routes() {
    const cont = document.getElementById("result_list");
    cont.innerHTML = "";

    const message = document.createElement("p");
    message.innerHTML = "Loading ...";

    cont.appendChild(message);
}

function show_error(error_msg) {
    const cont = document.getElementById("result_list");
    cont.innerHTML = "";

    const message = document.createElement("p");
    message.innerHTML = "Error al intentar obtener los datos del servidor: " + error_msg;
    cont.appendChild(message);
}

function show_routes(routes) {
    const cont = document.getElementById("result_list");
    cont.innerHTML = "";

    const grid = document.createElement("ul");
    grid.classList.add("result_grid")

    routes.forEach((route) => {
        const li = createRouteLi(route);
        grid.append(li);
        li.addEventListener("click", (event) => {
            // Show modal window with route data
            createRouteItem(route);
            modal.style.display = "block";
        })
    })

    cont.appendChild(grid);
}

