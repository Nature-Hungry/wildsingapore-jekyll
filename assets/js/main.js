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
      window.open(targetUrl, "_blank")
      overlay.classList.remove('show')
    }, 1500);
  }
});

// Shared lightbox: powers image galleries, inline article images and cover images alike.
(() => {
  const LIGHTBOX_IMAGE_SELECTOR = [
    '.gallery-image',
    '.coverimg img',
    '.post-cover-img',
    '.species-cover',
    '.ows2-cover img',
    '.species-header img',
    '.page-article img',
    '.article-body img',
    '.main-content img',
    '.contributor-article__content img',
    '.forteacher-article__content img',
    '.group-article__content img',
    '.ows2-content img',
    '.home-extra img',
  ].join(',');

  // Thumbnails/controls that happen to sit inside the selectors above but should keep their own behaviour.
  const LIGHTBOX_EXCLUDE_SELECTOR = [
    '#map',
    '.entry-summary-card',
    '.entry-summary-grid-item',
    '.entry-summary-row',
    '.contributor-preview',
    '.forindividual-preview',
    '.forteacher-preview',
    '.lastphotoindex-grid',
    '.pig-wrap',
    '.content-grid',
    'nav',
  ].join(',');

  const createLightbox = () => {
    if (document.querySelector('.gallery-lightbox')) return;

    const lightbox = document.createElement('div');
    lightbox.className = 'gallery-lightbox';
    lightbox.setAttribute('aria-hidden', 'true');
    lightbox.innerHTML = `
        <button class="gallery-lightbox-close" type="button" aria-label="Close enlarged image">&times;</button>
        <img class="gallery-lightbox-image" alt="">
    `;
    document.body.appendChild(lightbox);

    const closeLightbox = () => {
        lightbox.classList.remove('is-open');
        lightbox.classList.remove('is-zoomed');
        lightbox.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('gallery-lightbox-open');
        lightbox.querySelector('.gallery-lightbox-image').style.transform = '';
    };

    // Pans the zoomed image so the point under the cursor shifts into view: the cursor's
    // position within the viewport maps to how far the oversized image is shifted.
    const panToCursor = (clientX, clientY) => {
        const image = lightbox.querySelector('.gallery-lightbox-image');
        const overflowX = Math.max(0, image.naturalWidth - window.innerWidth);
        const overflowY = Math.max(0, image.naturalHeight - window.innerHeight);
        const ratioX = clientX / window.innerWidth;
        const ratioY = clientY / window.innerHeight;
        image.style.transform = `translate(${-overflowX * ratioX}px, ${-overflowY * ratioY}px)`;
    };

    // The image fills the lightbox box via object-fit:contain, so its element bounds can be
    // larger than the actual visible picture (letterboxing). Compute the real visible rect
    // so clicks on the letterbox padding still count as clicking the backdrop.
    const isInsideVisibleImage = (img, x, y) => {
        const rect = img.getBoundingClientRect();
        if (!img.naturalWidth || !img.naturalHeight) return x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom;

        const naturalRatio = img.naturalWidth / img.naturalHeight;
        const boxRatio = rect.width / rect.height;
        let renderedWidth = rect.width;
        let renderedHeight = rect.height;
        if (naturalRatio > boxRatio) {
            renderedHeight = rect.width / naturalRatio;
        } else {
            renderedWidth = rect.height * naturalRatio;
        }
        const left = rect.left + (rect.width - renderedWidth) / 2;
        const top = rect.top + (rect.height - renderedHeight) / 2;
        return x >= left && x <= left + renderedWidth && y >= top && y <= top + renderedHeight;
    };

    lightbox.addEventListener('click', (event) => {
        if (event.target.closest('.gallery-lightbox-close')) return;
        const image = lightbox.querySelector('.gallery-lightbox-image');
        if (event.target === image && isInsideVisibleImage(image, event.clientX, event.clientY)) {
            lightbox.classList.toggle('is-zoomed');
            if (lightbox.classList.contains('is-zoomed')) {
                panToCursor(event.clientX, event.clientY);
            } else {
                image.style.transform = '';
            }
        } else {
            closeLightbox();
        }
    });

    lightbox.addEventListener('mousemove', (event) => {
        if (lightbox.classList.contains('is-zoomed')) panToCursor(event.clientX, event.clientY);
    });

    document.addEventListener('click', (event) => {
        const image = event.target.closest(LIGHTBOX_IMAGE_SELECTOR);
        if (image && !image.closest(LIGHTBOX_EXCLUDE_SELECTOR)) {
            event.preventDefault();
            lightbox.querySelector('.gallery-lightbox-image').src = image.src;
            lightbox.querySelector('.gallery-lightbox-image').alt = image.alt;
            lightbox.querySelector('.gallery-lightbox-image').style.transform = '';
            lightbox.classList.remove('is-zoomed');
            lightbox.classList.add('is-open');
            lightbox.setAttribute('aria-hidden', 'false');
            document.body.classList.add('gallery-lightbox-open');
            return;
        }

        if (event.target.closest('.gallery-lightbox-close')) {
            closeLightbox();
        }
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && lightbox.classList.contains('is-open')) closeLightbox();
    });
  };

  if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', createLightbox, { once: true });
  } else {
      createLightbox();
  }
})();
