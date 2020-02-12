function resetUI() {


    var sliders = document.getElementsByTagName('input');
    var spans = document.getElementsByClassName('range-slider__value');
    for (var index = 0; index < sliders.length; ++index) {

        sliders[index].value = 0;
        spans[index].innerHTML = 0;
        applyNoFill(sliders[index]);
        
    }

}