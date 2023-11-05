const btnKick = document.querySelector("#kick");
const attr = document.createAttribute("value");
// const dateObj = new Date();
// attr.value = dateObj.toISOString().substring(0,23);
// console.log(btnKick);
// btnKick.setAttributeNode(attr);

btnKick.addEventListener('click', function displayDate() {
    
    // document.getElementById("B").innerHTML = Date();
    const dateObj = new Date();
    attr.value = dateObj.toISOString().substring(0,23);
    console.log(btnKick);
    btnKick.setAttributeNode(attr);
  
})