document.addEventListener('DOMContentLoaded', function () {
  const menuBtn = document.getElementById("menu-btn");
  const navLinks = document.getElementById("nav-links");
  const menuBtnIcon = menuBtn.querySelector("i");

  menuBtn.addEventListener("click", (e) => {
    navLinks.classList.toggle("open");

    const isOpen = navLinks.classList.contains("open");
    menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
  });

  navLinks.addEventListener("click", (e) => {
    navLinks.classList.remove("open");
    menuBtnIcon.setAttribute("class", "ri-menu-line");
  });

  const scrollRevealOption = {
    distance: "50px",
    origin: "bottom",
    duration: 1000,
  };

  ScrollReveal().reveal(".header__image img", {
    ...scrollRevealOption,
    origin: "right",
  });
  ScrollReveal().reveal(".header__content h2", {
    ...scrollRevealOption,
    delay: 500,
  });
  ScrollReveal().reveal(".header__content h1", {
    ...scrollRevealOption,
    delay: 1000,
  });

  ScrollReveal().reveal(".order__card", {
    ...scrollRevealOption,
    interval: 500,
  });

  ScrollReveal().reveal(".event__content", {
    duration: 1000,
  });

  // Form validation for reservation
  document.getElementById('reservation-form').addEventListener('submit', function(event) {
    const name = this[0].value;
    const email = this[1].value;
    const date = this[2].value;
    const time = this[3].value;
    const people = this[4].value;

    if (!name || !email || !date || !time || !people) {
      alert("Please fill in all fields.");
      event.preventDefault();
      return;
    }

    // Additional validation can be added here

  });

  // Order form modal and submission logic
  const modal = document.getElementById('order-modal');
  const closeBtn = document.getElementById('close-modal');
  const burgerInput = document.getElementById('burger-name');
  const orderForm = document.getElementById('order-form');

  document.querySelectorAll('.order__card button.btn').forEach(button => {
    button.addEventListener('click', (e) => {
      const card = e.target.closest('.order__card');
      const burgerName = card.querySelector('h4').innerText;
      burgerInput.value = burgerName;

      modal.style.display = 'flex';
    });
  });

  // Add click listeners to banner cards to open order modal with corresponding burger
  const bannerCards = document.querySelectorAll('.banner__card');
  const bannerBurgerMap = [
    "Cheese Onion Burger",
    "Classic Duo Burger",
    "Burger Ms.Spicy"
  ];
  bannerCards.forEach((card, index) => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', () => {
      burgerInput.value = bannerBurgerMap[index] || "";
      modal.style.display = 'flex';
    });
  });

  // Close modal
  closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  // Optional: Close modal if user clicks outside the modal content
  window.addEventListener('click', (e) => {
    if (e.target == modal) {
      modal.style.display = 'none';
    }
  });

  // Handle order form submit with validation
  orderForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('student-name').value.trim();
    const studentId = document.getElementById('SID/VID').value.trim();
    const item = burgerInput.value.trim();

    if (!name || !studentId || !item) {
      alert('Please fill in all fields.');
      return;
    }

    const orderData = { name, student_id: studentId, item };

    fetch('/api/order', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(orderData)
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert('Error: ' + data.error);
      } else {
        alert(data.message);
        modal.style.display = 'none';
        this.reset();
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Something went wrong!');
    });
  });
});