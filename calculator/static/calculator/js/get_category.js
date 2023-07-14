var cat_select = document.getElementById('category-select');
var url = "https://127.0.0.1:8000/api/v1/categories/";
var prod_select = document.getElementById('product-select');

cat_select.addEventListener('change', function(){
  var getValue = this.value;

  console.log( getValue );
});

