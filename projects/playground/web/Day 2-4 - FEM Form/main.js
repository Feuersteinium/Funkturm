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
gobackbtn.forEach( (btn, skipfor = "OFF") => {btn.addEventListener("click", () => {
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
    if (input["profile"] === undefined) {
        input["profile"] = 0
    }
    if (input["service"] === undefined) {
        input["service"] = 0
    }
    if (input["storage"] === undefined) {
        input["storage"] = 0
    }
    pricing = Number(input["plan"]) + Number(input["profile"]) + Number(input["service"]) + Number(input["storage"])
    if (input["monthly"] === "true") {
        document.querySelector("#f-step-4 #s4-plan").textContent = "(Monthly)"
        if (input["service"] !== "0") {
            document.querySelector("#f-step-4 div:nth-of-type(2)").style.display = "flex"
            document.querySelector("#f-step-4 div:nth-of-type(2) p:nth-child(2)").textContent = "1$/mo"
        }
        if (input["storage"] !== "0") {
        document.querySelector("#f-step-4 div:nth-of-type(3)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(3) p:nth-child(2)").textContent = "2$/mo"
        }
        if (input["profile"] !== "0") {
        document.querySelector("#f-step-4 div:nth-of-type(4)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(4) p:nth-child(2)").textContent = "2$/mo"
        }
        document.querySelector("#totalpricing").textContent = pricing.toString() + "$/mo"
        }
      
    else {
        console.log(pricing)
        pricing = pricing * 10
        console.log(pricing)
        document.querySelector("#f-step-4 #s4-plan").textContent = "(Annual)"
        if (input["service"] !== "0") {
            document.querySelector("#f-step-4 div:nth-of-type(2)").style.display = "flex"
            document.querySelector("#f-step-4 div:nth-of-type(2) p:nth-child(2)").textContent = "10$/yr"
        }
        if (input["storage"] !== "0") {
        document.querySelector("#f-step-4 div:nth-of-type(3)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(3) p:nth-child(2)").textContent = "20$/yr"
        }
        if (input["profile"] !== "0") {
        document.querySelector("#f-step-4 div:nth-of-type(4)").style.display = "flex"
        document.querySelector("#f-step-4 div:nth-of-type(4) p:nth-child(2)").textContent = "20$/yr"
        }
        document.querySelector("#totalpricing").textContent = pricing.toString() + "$/yr"
        }
    }


    document.querySelector(".boxy:nth-of-type(1)").addEventListener("click", () => {
        swto(1)
    })
        
    document.querySelector(".boxy:nth-of-type(2)").addEventListener("click", () => {
        swto(2)
    })
    document.querySelector(".boxy:nth-of-type(3)").addEventListener("click", () => {
        swto(3)
    })
    document.querySelector(".boxy:nth-of-type(4)").addEventListener("click", () => {
        swto(4)
    })

    function swto(slidenb) {
        console.log("triggered")
        let form = document.querySelector('#f-step-' + currentSlide.toString())
        let indicator = document.querySelector(".boxy:nth-child(" + currentSlide.toString() + ") h2")
        indicator.style.backgroundColor = ""
        form.style.display = "none"
        currentSlide = slidenb
        submit(currentSlide)
    }
})

