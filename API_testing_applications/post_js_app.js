data = {
    'name':'browser js','age':77,'city':'Thane'
}

url = 'http://127.0.0.1:8000/create/'

fetch(url,{
    method:'POST',
    headers : {
        'Content-Type' : 'application/json'
    },
    body : JSON.stringify(data)
})
.then(response=>response.json())
.then(data=>console.log(data))