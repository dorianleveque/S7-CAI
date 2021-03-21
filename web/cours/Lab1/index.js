// objet
const cube = document.querySelectorAll('.cube')
const faces = document.querySelectorAll('.face')
const standBackground = document.querySelector('#stand-background')

// Action
const playButton = document.querySelector('#playButton')
const stopButton = document.querySelector('#stopButton')



playButton.addEventListener('click', () => {
    cube.forEach((element) => {
        element.style.animationPlayState = 'running'
    })
    faces.forEach((element) => {
        element.style.animationPlayState = 'running'
    })
    standBackground.style.filter = 'none'
})

stopButton.addEventListener('click', () => {
    cube.forEach((element) => {
        element.style.animationPlayState = 'paused'
    })
    faces.forEach((element) => {
        element.style.animationPlayState = 'paused'
    })
    standBackground.style.filter = 'saturate(0%)'
})