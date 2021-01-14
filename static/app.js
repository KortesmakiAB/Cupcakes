const form = document.getElementById('cupcake_form');

form.addEventListener('submit', handleCupcakeForm);

async function handleCupcakeForm(e){
    e.preventDefault();

    const form_data = document.querySelectorAll('#cupcake_form input');
    const obj = Cupcake.makeCupcakeObj(form_data);
   
    const resp = await axios.post('/api/cupcakes', obj);
    Cupcake.appendCupcake(resp.data.cupcake);

    Cupcake.resetForm();
    
}

Cupcake.getCupcakes();