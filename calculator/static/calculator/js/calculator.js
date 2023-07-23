
const cat_select = document.getElementById('category-select');
const prod_select = document.getElementById('product-select');
const count_input = document.getElementById('counter');
const add_button = document.getElementById('add_button');
const result_button = document.getElementById('result_button');
const table = document.getElementById('cart_table');

const cart = [];
let current;

// Создает дефолтный тег опции...
let setDefaultOpt = function(text) {
    let defaul_opt = document.createElement('option')
    defaul_opt.textContent = text;
    defaul_opt.selected = 'selected';
    defaul_opt.value = 'default';
    return defaul_opt;
};

let createCurrProd = function() {
    let current_product = {};
    // вносим данные продукта в объект
    prod_select.addEventListener('change', function choose_product() {
        let product_id = this.value;
        let product_name;
        // можно было через бинарный поиск; не стал его реализовыть в js...
        for (item of this.options) {
            if (item.value == product_id) {
                product_name = item.text;
            };
        };
        if (product_id) {
            current_product.id = product_id;
            current_product.name = product_name;
        };
        });
    // вносим данные о количестве продукта...
    count_input.addEventListener('change', function input_count() {
        let count = this.value;
        if (count) {
            current_product.count = count;
    }; 
    });
    return current_product;
};
// динамически наполняет таблицу выбранными продуктами...
let createTuple = function(item) {
    title = item.name
    count = item.count
    let tr = document.createElement('tr');
    let td_name = document.createElement('td');
    let td_count = document.createElement('td');

    tr.class = 'table table-secondary';
    td_name.class = 'table table-secondary';
    td_count.class = 'table table-secondary';

    if (title && count) {
        td_name.append(title);
        td_count.append(count + ' гр.');
    };
    
    tr.append(td_name);
    tr.append(td_count);
   
    return tr;
};

// отправляет запросы и формирует дропдаун из ответа...
async function fetchHandler(url) {
    const response = await fetch(url);
    const data = await response.json();
    prod_select.textContent = '';
    let defaul_opt = setDefaultOpt("Выберите продукт")
    prod_select.append(defaul_opt);
    for (item of data) {
        opt = document.createElement('option');
        opt.value = item.id;
        opt.text = item.title;
        prod_select.append(opt);
    };
};

// Пользователь выбирает категорию, обработчик слушает...
cat_select.addEventListener('change', function select_cat() {
    let category_id = this.value;
    if (category_id) {
        let api_url = `http://127.0.0.1:8000/api/v1/products/category/${category_id}/`; // формируется запрос;
        fetchHandler(api_url); // запроос отправляется и на базе ответа формируется дропдаун спродуктами...
        // глобальный current принимает ссылку на объект...
        current = createCurrProd();  // начинается прослушивание дропдауна и ввода количества продукта и на основе выбраного продукта и количества  
    };
});

// начинается прослушивание кнопки и при ее нажатии активируется таблица и продукт добавляется в корзину. 
add_button.addEventListener('click', function fill_cart() {
    count_input.value = "";
    prod_select.value = "default";
    let new_current = {};
    if ( Object.keys(current).length == 3) {  // check!
        
        if (table.hidden) {
            table.hidden = false;
        };
        Object.assign(new_current, current);  // переменная хранит ссылку на объект, поэтому копируем
        cart.push(new_current);
        tr = createTuple(current);
        table.append(tr);
        
    } else {
        alert("Видимо вы забыли ввести какое-то значение!")
    };
});
    
// слушает кнопку рассчитать и при ее нажатии, массив с данными уходит на сервер в обработчик Django...
result_button.addEventListener('click', function sendJSON() {
    let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '');

    xhr.addEventListener('readystatechange', function() {
    if (xhr.readyState === 4) { 
        if (xhr.status === 200) {
            // Если есть вариант проще, предложите, мои знания js пока не так хороши...
            xhr.onload = function() {
                let  html = document.getElementsByTagName('html')[0]
                html.innerHTML = xhr.response;  // заменяем html полученнным от Django... 
              };
        } else {
            alert(xhr.status)
        }
    };
    }, false);

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.setRequestHeader('X-CSRFToken', csrf)
    if (cart.length > 0) {
        xhr.send(JSON.stringify(cart));  // нужно сериализовать объект в JSON строку...
        cart.length = 0  // обнуляем корзину...
    };
        });
    