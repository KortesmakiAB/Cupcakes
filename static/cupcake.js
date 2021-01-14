const cupcakesUL = document.getElementById('cupcake_list');

class Cupcake{
    
    static async getCupcakes(){
        const resp = await axios.get('/api/cupcakes');

        for (let cupcake of resp.data.cupcakes){
            this.appendCupcake(cupcake);
        }
    }
    
    static appendCupcake(obj){
        const li = document.createElement('li');
        li.innerText = obj.flavor;
        cupcakesUL.append(li);
    }
    
    static makeCupcakeObj(form_data){
        const obj = {};
        for (let field of form_data){
            obj[field.name] = field.value;
        }
        return obj;
    }

    static resetForm(){
        for (let field of form_data){
            field.value = '';
        }
    }
}



