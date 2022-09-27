$(document).ready(function () {
    
    // swiper
    let swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 10,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 10,
            },

            992: {
                slidesPerView: 2,
                spaceBetween: 10,
            },
            1024: {
                slidesPerView: 2.5,
                spaceBetween: 20,
            },
            1600: {
                slidesPerView: 2.5,
                spaceBetween: 30,
            }

        },
    });


    // aos
    AOS.init()


    let opener = document.querySelector(".opener");
    let closer = document.querySelector(".closer");
    let resNav = document.querySelector(".res-nav");
    let resLi = document.querySelectorAll(".res-nav ul li");

    opener.addEventListener("click", () => {
        if (resNav.style.transform = "translateY(-100%)") {
            resNav.style.transform = "translateY(0%)"
        } else {
            resNav.style.transform = "translateY(-100%)"
        }
    })
    closer.addEventListener("click", () => {
        if (resNav.style.transform = "translateY(0%)") {
            resNav.style.transform = "translateY(-100%)"
        } else {
            resNav.style.transform = "translateY(-100%)"
        }
    })

    resLi.forEach(li => {
        li.addEventListener('click', () => {
            if (resNav.style.transform = "translateY(0%)") {
                resNav.style.transform = "translateY(-100%)"
            } else {
                resNav.style.transform = "translateY(-100%)"
            }
        });
    });



    // contact modal
    let contactBtn = document.querySelector('.submit'),
        contactForm = document.querySelector('.submit-form'),
        contactModal = document.querySelector('.my-modal'),
        contactTitle = document.querySelector('.contact-title');


    contactBtn.addEventListener('click', () => {
        if (contactForm.style.display != 'none') {
            contactForm.style.display = 'none';
            contactModal.style.display = 'block';
            contactTitle.style.display = 'none'
        }
    })



    // picture
    let bigPic = document.querySelector('.big');
    let small1 = document.querySelector('.small-1'),
        small2 = document.querySelector('.small-2'),
        small3 = document.querySelector('.small-3'),
        bigAttr = bigPic.getAttribute('src'),
        small1Attr = small1.getAttribute('src'),
        small2Attr = small2.getAttribute('src'),
        small3Attr = small3.getAttribute('src');
    

    small1.addEventListener('click', () => {
        bigPic.setAttribute('src', small1Attr);
        bigPic.style.filter = 'opacity(0.5)';
        bigPic.style.transition = '0.5s ease';
        setTimeout(() => {
            bigPic.style.filter = 'opacity(1)';
        }, 400);

    })
    small2.addEventListener('click', () => {
        bigPic.setAttribute('src', small2Attr);
        bigPic.style.filter = 'opacity(0.5)';
        bigPic.style.transition = '0.5s ease';
        setTimeout(() => {
            bigPic.style.filter = 'opacity(1)';
        }, 400);
    })
    small3.addEventListener('click', () => {
        bigPic.setAttribute('src', small3Attr);
        bigPic.style.filter = 'opacity(0.5)';
        bigPic.style.transition = '0.5s ease';
        setTimeout(() => {
            bigPic.style.filter = 'opacity(1)';
        }, 400);
    })



});