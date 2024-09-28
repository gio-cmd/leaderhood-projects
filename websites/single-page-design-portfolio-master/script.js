const arrowLeft = document.getElementById('arrow-left');
const arrowRight = document.getElementById('arrow-right');

const list = [
    'perfume.jpg',
    'name.jpg',
    'image.png',
    'Q&A.jpg',
    'qr.jpg',
    'nft.png'
];
const listCodes = [
    'https://65c0d4ca5707f50f7dff7709--dreamy-meerkat-01c1fc.netlify.app/',
    'https://65bba268b45aca0b7a466c4a--magenta-pithivier-ab26e9.netlify.app/',
    'https://65d399e8472a40126d0b7c13--spontaneous-bienenstitch-133909.netlify.app/',
    'https://65d3985975bf92169f0dcccd--charming-zabaione-470816.netlify.app/',
    'https://65ccfae1385ac20685a27693--comfy-cranachan-377344.netlify.app/',
    'https://65c0d6b77aff5211e70a49b4--lambent-quokka-fef9f8.netlify.app/'
];

const listLinks = [
    'https://github.com/gio-cmd/Solo_Projects/tree/main/Websites/social-links-profile-main',
    'https://github.com/gio-cmd/Solo_Projects/tree/main/Websites/social-links-profile-main',
    'https://github.com/gio-cmd/Solo_Projects/tree/main/Websites/recipe-page-main',
    'https://www.frontendmentor.io/solutions/frontend-mentor-faq-accordion-ZSIMNqKhf7',
    'https://www.frontendmentor.io/solutions/frontend-mentor-qr-code-component-bi9JG_r9Uh',
    'https://github.com/gio-cmd/Solo_Projects/tree/main/Websites/social-links-profile-main',
];

let number = 0;
const img = document.getElementById('slider');
const linkBtn = document.getElementById('button1');
const codeBtn = document.getElementById('button2');

function changeSlide(direction) {
    if (direction === 'next') {
        number++;
        if (number >= list.length) {
            number = 0;
        }
    } else {
        number--;
        if (number < 0) {
            number = list.length - 1;
        }
    }
    img.setAttribute('src', list[number]);
    linkBtn.setAttribute('href', listLinks[number]);
    codeBtn.setAttribute('href', listCodes[number]);
}

function autoSlide() {
    changeSlide('next');
}

img.setAttribute('src', list[number]);
linkBtn.setAttribute('href', listLinks[number]);
codeBtn.setAttribute('href', listCodes[number]);

arrowLeft.addEventListener('click', function () {
    changeSlide('prev');
});

arrowRight.addEventListener('click', function () {
    changeSlide('next');
});

const intervalId = setInterval(autoSlide, 3000);


