
const textarea = document.querySelector('textarea');
const submit = document.querySelector('button');

submit.addEventListener('click',(event) => {
	const value =  textarea.value;
	if(value != ''){
		axios.post('https://localhost:5000/predict',{
			tweet : value
		}).then(response => {
			console.log(response.data);
		}).catch(err =>{
			console.log(err);
		})
	}
})