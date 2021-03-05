console.log("javascript run");
document.getElementById('submit').addEventListener('click',check);
function register() {
  let email=document.getElementById('email').value
  let name=document.getElementById('name').value
  let password=document.getElementById('password').value
  let confirm_password=document.getElementById('confirmpassword').value
  const data= { method:'POST',
                mode:'no-cors',
               
                headers:{
                  'Content-Type':'application/json',
                  
                },

                  
                body:JSON.stringify({company_email:email,company_name:name,password:password})
                }

 
 console.log(data.body)
  fetch('http://localhost:7002/company_register/',)
    .then((res)=>{
      if(!res.ok){
        throw Error(res.statusText)
      }
      return res.json()    
    }).then((data)=>{
      console.log(data)
    }).catch((error)=>{console.log(error)})
}

function check() {
data={

	password:"nit123",
	company_name:"infosys",
	email:"prince.singh@gmail.com"
}

  
  axios.post('http://localhost:7002/company_register/',{"Access-Control-Allow-Origin": "*"})
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });   
}