
async function popular(){
    let  response= await fetch('http://127.0.0.1:5000/popular') // pairnoume ta data apo DB
    let popArray=await(response.json())
    let container = document.getElementById('athletes-container') // ftiaxnume container me data
    container.innerHTML=""  // adiazume to  mesa tou container gia na to gemisume swsta 
    for (let i=0;i<popArray.length;i++){ // gemizw kathe karta name, photo, likes
        let athlete=popArray[i] // athlete exei 1 json item, ara athlete.likes. athlete.photo klp
        container.innerHTML+= generateCard(athlete)
    }
}

async function search(){

    query=document.getElementById('search-input').value
    // sto items, sto searchbar, pernume to value apo oti grapsei mesa sto bar .

  let response=await fetch('http://127.0.0.1:5000/search?name=' + query)
  // psaxnume oti egrapse an yparxei sthn db 

let athletes= await response.json()

  let container = document.getElementById('athletes-container'); // ftiaxnume container me data
    container.innerHTML=""
    // ftiaxnume xwro na boun oi kartes, kai adiazume tocontainer apo palies.

  for (let i=0;i<athletes.length;i++)
  {
 container.innerHTML+=generateCard(athletes[i])

  }
}


 function generateCard( athlete){ // pairnei 1 item athlete apo to json kai 
    // xrhsimopoiwntas ta athlete.photo, athlete.name etc ftiaxnei thn karta
    // vazw olh thn karta me backticks kai stis metavlites vazw ${athlete.field }
return `<div class="col">
                    <div class="card h-100" id="card-${athlete._id}">
                        <img src="${athlete.photo}" class="card-img-top" alt="${athlete.name}" style="height: 200px; object-fit: ${athlete.name === 'Giannis Kallionakis' ? 'contain' : 'cover'}; object-position: top; background-color: ${athlete.name === 'Giannis Kallionakis' ? '#111' : 'transparent'};">
                        <div class="card-body">
                            <h5 class="card-title">${athlete.name}</h5>
                        </div>
                            <div class="card-footer bg-dark text-warning text-center">
                                <span> 💪 <span class="likes-counter">${athlete.likes} </span> likes </span>
                                <button onclick="like('${athlete._id}')" class="btn btn-sm btn-warning mt-1">Heavy! 💪</button>
                            </div>
                    </div>
                </div>  `
 }


window.onload = function() { // perimenei na fortwsei olh  h selida k meta trexei h function
    
    const urlParams = new URLSearchParams(window.location.search)
    if (!document.getElementById('search-input')) return  // elegxei an eimaste sto items.html ( mono to items exei search-input)
    const nameFromUrl = urlParams.get('name')
//epeidh an kapoios psaksei apo to homepage ton kanei transfer sto items pou ginete to search
// me to window.location.search krataei oti egrapse o allos ( dld oti einai meta to ?) dld to query string
//  to URLSearchParams pernei to query string kai to spaei se lista me metavlites, px name , status
// sto urlParams apothikeuontai oles oi metavlites tou query kai tis kanw access me to get .
    
    if (nameFromUrl) {
        //an vrei name sto query 
        document.getElementById('search-input').value = nameFromUrl
       // paei stou items to search kai vazei to name pou egrapse o allos sto homepage kai to psaxnei
        //mono tou
        search()}
        else{
            search()
        }
        
    
}

if (!document.getElementById('search-input')) {  // an eimaste sto homepage, ( apousia search input) trexei to popular()
    popular()
}

async function like(id) {
    let response = await fetch('http://127.0.0.1:5000/like',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id: id})
    })
    let data = await response.json()

    let counter = document.querySelector(`#card-${id} .likes-counter`)
    counter.innerText = parseInt(counter.innerText) + 1
}