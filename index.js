let $fav = document.querySelector('.fav')
let $favAll = document.querySelectorAll(".fav")






function genID(el) {
el.forEach(element => {
  element.id = `${Math.round(Math.random()*100)}`
  element.addEventListener("click",function(){
    element.classList.toggle("active");
  })
});
}
genID($favAll)

