const msg = document.querySelector('#msg').textContent;
console.log(msg)
if (msg == 'notloggedin'){
    alert('You must be logged in !');
    window.location.href = '/';
}










import { movies } from "/statics/js/movies.js"
import { moviesArray } from "/statics/js/moviesArray.js"




const movieInput = document.getElementById('movieInput')
const movieList = document.getElementById('movieList')










for (let i = 0; i < moviesArray.length; i++) {
    let item = movies[i]
    let itemIMG = moviesArray.find(a => Object.keys(a)[0] === item);
    itemIMG = itemIMG[item]
    const img = document.createElement('img');
    img.src = itemIMG
    img.classList.add('movieItemsIMG')
    const p = document.createElement('p');
    p.textContent = item;
    const a = document.createElement('a');
    let url = './result.html?movieName=' + item
    a.href = url
    a.classList.add('movieItems')
    a.appendChild(img);
    a.appendChild(p);
    movieList.appendChild(a)
}





movieInput.addEventListener('keyup', () => {
    const searchText = movieInput.value.toLowerCase();
    if (searchText == '') {
        for (let i = 0; i < moviesArray.length; i++) {
            let item = movies[i]
            let itemIMG = moviesArray.find(a => Object.keys(a)[0] === item);
            itemIMG = itemIMG[item]
            const img = document.createElement('img');
            img.src = itemIMG
            img.classList.add('movieItemsIMG')
            const p = document.createElement('p');
            p.textContent = item;
            const a = document.createElement('a');
            let url = './result.html?movieName=' + item
            a.href = url
            a.classList.add('movieItems')
            a.appendChild(img);
            a.appendChild(p);
            movieList.appendChild(a)
        }
    }
    const filteredData = movies.filter(item => item.toLowerCase().includes(searchText));
    movieList.innerHTML = '';
    filteredData.forEach(item => {
        let itemIMG = moviesArray.find(a => Object.keys(a)[0] === item);
        itemIMG = itemIMG[item]
        const img = document.createElement('img');
        img.src = itemIMG
        img.classList.add('movieItemsIMG')
        const p = document.createElement('p');
        p.textContent = item;
        const a = document.createElement('a');
        let url = './result.html?movieName=' + item
        a.href = url
        a.classList.add('movieItems')
        a.appendChild(img);
        a.appendChild(p);
        movieList.appendChild(a)
    });
})
