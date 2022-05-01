const btn = document.querySelectorAll('#click');
const clicked = document.querySelector('.clicked');
const newsTitle = document.querySelectorAll('.news-title');
const newsDes = document.querySelectorAll('.news-des');
const openModalButtons = document.querySelectorAll('[data-modal-target]');
const closeModalButtons = document.querySelectorAll('[data-close-button]');
const overlay = document.getElementById('overlay');

for (nt of newsTitle) {
  titleContent = nt.textContent;

  // console.log(titleContent);

  len = nt.textContent.length;
  if (len > 80) {
    content_dis = titleContent.slice(0, 80);
    // console.log(`${content_dis}...`);
    nt.innerText = `${content_dis}...`;
  }
  // console.log(titleContent.length);
}

for (nt of newsDes) {
  DesContent = nt.textContent;

  console.log(DesContent);

  len = DesContent.length;
  if (len > 120) {
    content_dis = DesContent.slice(0, 80);
    console.log(`${content_dis}...`);
    nt.innerText = `${content_dis}...`;
  }
  console.log(DesContent.length);
}
// btn.addEventListener('click', () => {
//   alert('clicked');
// });

clicked.addEventListener('click', () => {
  alert('clicked');
});

openModalButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const modal = document.querySelector(button.dataset.modalTarget);
    openModal(modal);
  });
});

overlay.addEventListener('click', () => {
  const modals = document.querySelectorAll('.modal.active');
  modals.forEach((modal) => {
    closeModal(modal);
  });
});

closeModalButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const modal = button.closest('.modal');
    closeModal(modal);
  });
});

function openModal(modal) {
  if (modal == null) return;
  modal.classList.add('active');
  overlay.classList.add('active');
}

function closeModal(modal) {
  if (modal == null) return;
  modal.classList.remove('active');
  overlay.classList.remove('active');
}
