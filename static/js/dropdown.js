
const dropdownButton = document.getElementById('dropdown-button');
const dropdownMenu = document.getElementById('dropdown-menu');
const msg = document.getElementById('message')

dropdownButton.addEventListener('click', () => {
  dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
});


setInterval(() => {
  msg.style.display = "none"
}, 5000);