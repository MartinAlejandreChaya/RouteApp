const SEARCH_INPUT_EXAMPLES = [
    "Sierra Nevada", "Pirineos", "Navacerrada"
]

window.onload = () => {


    // Listen to search event
    const search_input = document.getElementById("search_input");
    search_input.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            const req_data = {"search_title": search_input.value};
            console.log("Sending GET request for data: ", req_data)
            fetch("/search_routes", {
                "method": "POST",
                "headers": {"Content-Type": "application/json"},
                "body": JSON.stringify(req_data),
            }).then( response => response.json() ).then(data => {
                console.log("Response recieved", data)
            });
        }
    });

    animate_placeholder_input(search_input, SEARCH_INPUT_EXAMPLES);
}



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