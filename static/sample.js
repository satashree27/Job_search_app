const jobs = [
    {job: 'plumber'},
    {job: 'miner'}
];

const list = document.getElementById('list')

function setList(group){

    clearList(group);
    for(const j of jobs){
        const item = document.createElement('li');
        item.classList.add('list-group-item');
        const text = document.createTextNode(j, job);
        item.appendChild(text);
        list.appendChild(item);
    }
    if(group.length === 0){
        setNoresults();
    }

}

function clearList(){

    while(list.firstChild){
        list.removeChild(list.firstChild);
    }
}

function setNoresults(){

    const item = document.createElement('li');
    item.classList.add('list-group-item');
    const text = document.createTextNode('No results found');
    item.appendChild(text);
    list.appendChild(item);
}

function getRelevance(value, searchTerm){

    if(value === searchTerm){
        return 2;
    }
    else if(value.startsWith(searchTerm)){
        return 1;
    }
    else if(value.includes(searchTerm)){
        return 0;
    }
    else{
        return -1;
    }
}

const searchInput = document.getElementById("search");

searchInput.addEventListener("input", ()=>{
    let value = EventTarget.value;
    if(value && value.trim().length > 0){

        value = value.trim().toLowerCase();
        setList(jobs.filter(j => {
            return j.job.includes(value);
        }).sort((j1, j2)=>{
            return getRelevance(j2.job, value)-getRelevance(j1.job, value);
        }));
    }
    else{
        clearList();
    }
});