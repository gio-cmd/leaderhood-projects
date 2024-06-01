const image = document.getElementById('pic');

const list = [
    '/photos/perfume.jpg',
    '/photos/Q&A.jpg',
    '/photos/qr.jpg',
    '/photos/nft.png'
];

let number = 0;

image.addEventListener('click', () => {
    number = (number + 1) % list.length;
    image.setAttribute('src', list[number]);
});
