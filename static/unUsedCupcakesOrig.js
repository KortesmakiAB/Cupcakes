const form = document.getElementById('cupcake_form');
const cupcakesUL = document.getElementById('cupcake_list');

// query the API to get the cupcakes and adds to the page
async function getCupcakes(){
    const url = '/api/cupcakes';
    const resp = await axios.get(url);
    for (let cupcake of resp.data.cupcakes){
        appendCupcake(cupcake);
    }
}

function appendCupcake(obj){
    const li = document.createElement('li');
    li.innerText = obj.flavor;
    cupcakesUL.append(li);
}

form.addEventListener('submit', submitNewCupcakeForm);

async function submitNewCupcakeForm(e){
    e.preventDefault();

    const form_data = document.querySelectorAll('#cupcake_form input')
    const obj = makeCupcakeObj(form_data);
   
    const resp = await axios.post('/api/cupcakes', obj);
    appendCupcake(resp.data.cupcake)

    for (let field of form_data){
        field.value = "";
    }
}

function makeCupcakeObj(form_data){
    const obj = {};
    for (let field of form_data){
        obj[field.name] = field.value;
    }
    return obj;
}


getCupcakes()
