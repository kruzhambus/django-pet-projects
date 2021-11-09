

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Ви хочете пройти тест "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>Складність: <b>${difficulty}</b></li>
                <li>Кільуість питань: <b>${numQuestions}</b></li>
                <li>Прохідний бал: <b>${scoreToPass}%</b></li>
                <li>Час: <b>${time} min</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{


        window.location.href = '/'+ 'quiz'+ '/' + pk
    })
}))


