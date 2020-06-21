$(document).ready(function(){
var form =$('#by_product');
console.log(form)
form.on('submit',function(e){
    e.preventDefault();
    var select = $('#size option:selected');
    var size  = select.val();
    console.log(size);
    var submit_btn = $('#submit_btn');
    var product_image = submit_btn.data("product_image");
    var product_title =  submit_btn.data("product_title");
    var product_prace =  submit_btn.data("product_prace");
    var product_slug = submit_btn.data("product_slug");
    console.log(product_prace)
    console.log(product_title)
    console.log(product_image)
    console.log(product_slug)
    var opacity = 0;
    var w = 0;
function addproductAnimation() {
     add_product.style.opacity = opacity;
     opacity =  opacity + 0.1;
     w++;
    if( w < 10 ){
        setTimeout( addproductAnimation, 50 );
        
    }  
};


addproductAnimation()

    var data = {};
    data.product_image = product_image;
    data.product_size_id = size;
    data.product_title = product_title;
    data.product_prace = product_prace;
    data.product_slug = product_slug;
    var csrf_token = $('#by_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
    var url = form.attr("action"); 
    console.log(data)
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            console.log("OK");},
        
        error: function(){
            console.log("error");
        },
            
        })   



    $('.cart_quantity').append('<p>'+1+'   <p>')
})
}
);


$('.cart').on(' click', function(){
   
    $('.cart-item').removeClass('hidden');

});





 






$(document).ready(function(){
    var form =$('#orders');
    console.log(form)
    form.on('submit',function(e){
        e.preventDefault();
        var firstname = $('#firstname');
        var firstname = firstname.val();
        var lastname = $('#lastname');
        var lastname = lastname.val();
        var adress = $('#adress');
        var adress = adress.val();
        var phone = $('#phone');
        var phone = phone.val();
        var submit_orders = $('#submit_orders');
        var cart_product =  submit_orders.data("cart_product");
        var index_url= submit_orders.data("index_url");        
        console.log(cart_product);
        console.log(firstname);
        console.log(lastname);
        console.log(adress);
        console.log(phone);
        orders_complite()

        var data = {};
        data.firstname = firstname;
        data.lastname = lastname;
        data.adress=adress;
        data.phone=phone;
        data.product_title=cart_product;
        var csrf_token = $('#orders [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action"); 
        console.log(data)
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                       ok()
                
                console.log("OK");},
                
            
            error: function(){
                console.log("error");
            },
                
            })   
    
    })})
 
    $(document).ready(function(){
        var form =$('#quantity_product');
        console.log(form)
        form.on('submit',function(e){
            e.preventDefault();
            var quantity_product_num = $('#quantity_product_num');
            var quantity_product_num = quantity_product_num.val();
            var submit_quantity_product = $('#submit_quantity_product');
            var quantity_size =  submit_quantity_product.data("quantity_size");
            var quantity_id = submit_quantity_product.data("quantity_id");
            console.log(quantity_size)
            console.log(quantity_product_num)
            console.log(quantity_id)
    
            var data = {};
            data.quantity_product_num = quantity_product_num;
            data.quantity_size = quantity_size;
            data.quantity_id = quantity_id;
            var csrf_token = $('#quantity_product [name="csrfmiddlewaretoken"]').val();
                data["csrfmiddlewaretoken"] = csrf_token;
            var url = form.attr("action"); 
            console.log(data)
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    alert(".!.")
                    
                    console.log("OK");},
                    
                
                error: function(){
                    console.log("error");
                },
                    
                })   
        
        })})    

        var multiItemSlider = (function () {
            return function (selector, config) {
              var
                _mainElement = document.querySelector(selector), // основный элемент блока
                _sliderWrapper = _mainElement.querySelector('.slider_detail__wrapper'), // обертка для .slider-item
                _sliderItems = _mainElement.querySelectorAll('.slider_detail__item'), // элементы (.slider-item)
                _sliderControls = _mainElement.querySelectorAll('.slider_detail__control'), // элементы управления
                _sliderControlLeft = _mainElement.querySelector('.slider_detail__control_left'), // кнопка "LEFT"
                _sliderControlRight = _mainElement.querySelector('.slider_detail__control_right'), // кнопка "RIGHT"
                _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // ширина обёртки
                _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // ширина одного элемента    
                _positionLeftItem = 0, // позиция левого активного элемента
                _transform = 0, // значение транфсофрмации .slider_wrapper
                _step = _itemWidth / _wrapperWidth * 100, // величина шага (для трансформации)
                _items = []; // массив элементов
              // наполнение массива _items
              _sliderItems.forEach(function (item, index) {
                _items.push({ item: item, position: index, transform: 0 });
              });
      
              var position = {
                getMin: 0,
                getMax: _items.length - 1,
              }
      
              var _transformItem = function (direction) {
                if (direction === 'right') {
                  if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) >= position.getMax) {
                    return;
                  }
                  if (!_sliderControlLeft.classList.contains('slider_detail__control_show')) {
                    _sliderControlLeft.classList.add('slider_detail__control_show');
                  }
                  if (_sliderControlRight.classList.contains('slider_detail__control_show') && (_positionLeftItem + _wrapperWidth / _itemWidth) >= position.getMax) {
                    _sliderControlRight.classList.remove('slider_detail__control_show');
                  }
                  _positionLeftItem++;
                  _transform -= _step;
                }
                if (direction === 'left') {
                  if (_positionLeftItem <= position.getMin) {
                    return;
                  }
                  if (!_sliderControlRight.classList.contains('slider_detail__control_show')) {
                    _sliderControlRight.classList.add('slider_detail__control_show');
                  }
                  if (_sliderControlLeft.classList.contains('slider_detail__control_show') && _positionLeftItem - 1 <= position.getMin) {
                    _sliderControlLeft.classList.remove('slider_detail__control_show');
                  }
                  _positionLeftItem--;
                  _transform += _step;
                }
                _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
              }
      
              // обработчик события click для кнопок "назад" и "вперед"
              var _controlClick = function (e) {
                if (e.target.classList.contains('slider_detail__control')) {
                  e.preventDefault();
                  var direction = e.target.classList.contains('slider_detail__control_right') ? 'right' : 'left';
                  _transformItem(direction);
                }
              };
      
              var _setUpListeners = function () {
                // добавление к кнопкам "назад" и "вперед" обрботчика _controlClick для событя click
                _sliderControls.forEach(function (item) {
                  item.addEventListener('click', _controlClick);
                });
              }
      
              // инициализация
              _setUpListeners();
      
              return {
                right: function () { // метод right
                  _transformItem('right');
                },
                left: function () { // метод left
                  _transformItem('left');
                }
              }
      
            }
          }());
      
          var slider = multiItemSlider('.slider_detail')



 
    