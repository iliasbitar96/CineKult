document.getElementById("choice-select").addEventListener("change", function() {
    let category = document.getElementById("category-select");
    let actor = document.getElementById("actor-div");
    let director = document.getElementById("director-div");
    let production = document.getElementById("production-div");

    if (this.value === "category") {
        category.style.display = "inline";
        actor.style.display = "none";
        director.style.display = "none";
        production.style.display = "none";
    }
    if (this.value === "actor") {
        actor.style.display = "inline";
        category.style.display = "none";
        director.style.display = "none";
        production.style.display = "none";
    }
    if (this.value === "director") {
        director.style.display = "inline";
        category.style.display = "none";
        actor.style.display = "none";
        production.style.display = "none";
    }
    if (this.value === "production") {
        production.style.display = "inline";
        category.style.display = "none";
        director.style.display = "none";
        actor.style.display = "none";
    }
});