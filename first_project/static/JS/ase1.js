function fade() {
    $('.img1').fadeIn().delay(5000).fadeOut();
    $('.img2').delay(5000).fadeIn().delay(5000).fadeOut();
    $('.img3').delay(10000).fadeIn().delay(5000).fadeOut(fade);
    $('.img4').fadeIn().delay(5000).fadeOut();
    $('.img5').fadeIn().delay(5000).fadeOut();
    $('.img6').fadeIn().delay(5000).fadeOut();
    $('.img7').fadeIn().delay(5000).fadeOut();
    $('.img8').fadeIn().delay(5000).fadeOut();
}
fade();
