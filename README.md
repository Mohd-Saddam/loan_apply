# Flask Loan apply,approve and list user who applied API APP

## Running the Project Locally

Install the requirements:

```
 install the module
```

Finally, run the development server:

```bash
python main.py

```
``` Use Postman```

The API endpoints will be available at
To loan apply the user POST **http://127.0.0.1:5000/api/apply_loan**    
Body : {
	"name":"ABC",
	"email":"abc@gmail.com",
	"address":"New Dehli",
	"phone":"+91-9897551230",
	"salary":"25500.5",
	"occupation":"job"
}

server resopnse  = {
    "msg": "Apply loan successfully!"
}
if user exist={
    "msg": "Email already exists"
}

To approve loan  PUT **http://127.0.0.1:5000/api/approve_loan**
{
	"email":"abc@gmail.com"
}
if email not found={
    "msg": "Email does not exists"
}

To get list who applied 
http://127.0.0.1:5000/api/getUserLoanApply
get result:-
{
    "ApplyLoan": [
        {
			"user_name": "ABC"
			"email": "abc@gmail.com",
            "address": "New Dehli",
            "curr_salary": 25500.5,
            "occupation": "job",
            "phone": "+91-9897551230",
            
        },
		{
			"user_name": "ABC1"
			"email": "abc1@gmail.com",
            "address": "New Dehli",
            "curr_salary": 20000,
            "occupation": "job",
            "phone": "+91-9897551230",
            
        }
    ],
    "toltaluser": 2
}