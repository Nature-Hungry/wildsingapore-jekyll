


let overlay = document.getElementById("redirect-overlay")
document.addEventListener("DOMContentLoaded", function(){
    overlay = document.getElementById("redirect-overlay")
    overlay.classList.remove('show');
});



const redirectMap = {
  "sgfishesabovewater.blogspot.com":{
    "logo":"",
  }
}


document.body.addEventListener('click', function(event) {
  // 2. Check if the clicked element (or its closest ancestor) is a transition link
  const link = event.target.closest('a[external]');
  
  if (link) {
    // 3. Override the default redirect
    event.preventDefault();
    const targetUrl = link.href;
    console.log(link);
    
    
    // 4. Trigger transition animation
    overlay.classList.add('show');
    overlay.replaceChildren()
    overlay.insertAdjacentHTML('beforeend', `
      <img src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.25/css/loading.gif"/>
      <p>Redirecting to ${link.getAttribute("external")}</p>
    `);
    
    // 5. Redirect after transition finishes
    console.log("Redirecting to ", link.getAttribute("external"))
    setTimeout(() => {
      window.location.href = targetUrl;
    }, 1500);
  }
});