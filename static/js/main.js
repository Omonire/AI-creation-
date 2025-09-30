document.addEventListener('DOMContentLoaded', () => {

    // 1. Navigation bar scroll effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('nav-scrolled');
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    });

    // 2. Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // 3. Hero section typing effect
    const typingElement = document.getElementById('typing-effect');
    const roles = ["Certified Ethical Hacker", "Python Programmer", "Cyber Security Analyst", "Data Visualization Expert"];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function type() {
        const currentRole = roles[roleIndex];
        if (isDeleting) {
            typingElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingElement.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
        }

        if (!isDeleting && charIndex === currentRole.length) {
            isDeleting = true;
            setTimeout(type, 2000); // Pause at end of word
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            setTimeout(type, 500); // Pause before new word
        } else {
            const typingSpeed = isDeleting ? 75 : 150;
            setTimeout(type, typingSpeed);
        }
    }
    type();

    // 4. Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 5. Contact form submission
    const contactForm = document.getElementById('contact-form');
    const formFeedback = document.getElementById('form-feedback');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);

        fetch('/contact', {
            method: 'POST',
            body: new URLSearchParams(formData)
        })
        .then(response => response.json())
        .then(data => {
            formFeedback.textContent = data.message;
            contactForm.reset();
            setTimeout(() => {
                formFeedback.textContent = '';
            }, 5000);
        })
        .catch(error => {
            console.error('Error:', error);
            formFeedback.textContent = 'An error occurred. Please try again later.';
        });
    });

});