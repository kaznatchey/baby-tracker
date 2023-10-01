const btnKick = document.querySelector("#kick");
const attr = document.createAttribute("value");
attr.value=Date();
console.log(btnKick);
btnKick.setAttributeNode(attr);


// btnKick.addEventListener('click', function displayDate() {
    
//     document.getElementById("B").innerHTML = Date();
  
// })