let currentSlide = 1;
let details = {}

document.addEventListener('DOMContentLoaded', () => {

    function submit(slide) {
        if (currentSlide <= 0) {
            currentSlide = 1
        }

        if (currentSlide === 4) {
            pricecalculation(details)
        }


        let form = document.querySelector('#f-step-' + slide.toString())
        form.style.display = "flex"
        let indicator = document.querySelector(".boxy:nth-child(" + currentSlide.toString() + ") h2")
        indicator.style.backgroundColor = "white"
        console.log(currentSlide + ">> Started Function")
        function triggerme(e) {
            e.preventDefault()
            let data = new FormData(form)        
            for (let loop of data.entries()) {
                details[loop[0]] = loop[1]
            }
            form.style.display = "none"
            indicator.style.backgroundColor = ""
            form.removeEventListener("submit", triggerme)
            currentSlide++
            console.log(details)
            console.log(currentSlide)

            // Recursion Protection

            if (currentSlide <= 5) {
                submit(currentSlide)
            }
            console.log("EXEC Submit DONE")

        }

        form.addEventListener("submit", triggerme)
           
    }
     /*   form.removeEventListener("submit", (e) => {
            e.preventDefault()
            let data = new FormData(form)        
            for (let loop of data.entries()) {
                details[loop[0]] = loop[1]
            }
            form.style.display = "none"
            currentSlide++
            console.log(details)
            console.log(currentSlide)
            console.log("Unreachable")
        })*/

    console.log(currentSlide + ">> INIT btw.")
    submit(currentSlide)
   
let gobackbtn = document.querySelectorAll(".btns button:first-child")
gobackbtn.forEach( (btn) => {btn.addEventListener("click", () => {
    if (currentSlide > 1) {
        let form = document.querySelector('#f-step-' + currentSlide.toString())
        let indicator = document.querySelector(".boxy:nth-child(" + currentSlide.toString() + ") h2")
        indicator.style.backgroundColor = ""
        form.style.display = "none"
        currentSlide--
        console.log(currentSlide + ">> BTN triggered")
        submit(currentSlide)
    }
})
})

function pricecalculation(input) {
    console.log("PC RUNNING")
    pricing = input["plan"] + input["profile"] + input["service"] + input["storage"]
    if (input["monthly"] === "true") {
        document.querySelector("#f-step-4 #s4-plan").textContent = "(Monthly)"
        if (input["service"] !== "0") {
            console.log("PC RUNNING 1 ")
            document.querySelector("#f-step-4 div:nth-of-type(2)").style.display = "flex"
            document.querySelector("#f-step-4 div:nth-of-type(2) p:nth-child(2)").textContent = "1$/mo"
        }
        if (input["storage"] !== "0") {
            console.log("PC RUNNING 2")
        document.querySelector("#f-step-4 div:nth-of-type(3)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(3) p:nth-child(2)").textContent = "2$/mo"
        }
        if (input["profile"] !== "0") {
            console.log("PC RUNNING 3")
        document.querySelector("#f-step-4 div:nth-of-type(4)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(4) p:nth-child(2)").textContent = "2$/mo"
        }
        }
      
    else {
        pricing = pricing * 10
        document.querySelector("#f-step-4 #s4-plan").textContent = "(Annual)"
        if (input["service"] !== "0") {
            console.log("PC RUNNING 1 ")
            document.querySelector("#f-step-4 div:nth-of-type(2)").style.display = "flex"
            document.querySelector("#f-step-4 div:nth-of-type(2) p:nth-child(2)").textContent = "10$/yr"
        }
        if (input["storage"] !== "0") {
            console.log("PC RUNNING 2")
        document.querySelector("#f-step-4 div:nth-of-type(3)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(3) p:nth-child(2)").textContent = "20$/yr"
        }
        if (input["profile"] !== "0") {
            console.log("PC RUNNING 3")
        document.querySelector("#f-step-4 div:nth-of-type(4)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(4) p:nth-child(2)").textContent = "20$/yr"
        }
        }
    }
})
