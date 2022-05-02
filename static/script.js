const newsTitle = document.querySelectorAll('.news-title');
const newsDes = document.querySelectorAll('.news-des');
const opens = document.querySelectorAll('.open');
const modals = document.querySelectorAll('.modal-bg');
const modalClose = document.querySelectorAll('.modal-close');

for (nt of newsTitle) {
  titleContent = nt.textContent;

  len = nt.textContent.length;
  if (len > 80) {
    content_dis = titleContent.slice(0, 80);
    nt.innerText = `${content_dis}...`;
  }
}

for (nt of newsDes) {
  DesContent = nt.textContent;
  console.log(DesContent);
  len = DesContent.length;
  console.log(len);
  if (len > 120) {
    content_dis = DesContent.slice(0, 80);
    nt.innerText = `${content_dis}...`;
    console.log(DesContent);
  }
  console.log(DesContent);
}

opens.forEach((btn, index) => {
  btn.addEventListener('click', () => {
    console.log(`${index}: clicked`);
    const modalClicked = modals[index];
    modalClicked.classList.add('bg-active');
  });
});

modalClose.forEach((ele, index) => {
  ele.addEventListener('click', () => {
    const modalClicked = modals[index];
    modalClicked.classList.remove('bg-active');
  });
});
