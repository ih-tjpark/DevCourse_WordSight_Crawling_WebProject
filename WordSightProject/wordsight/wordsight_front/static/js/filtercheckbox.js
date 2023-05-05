document.getElementById("interest_all").addEventListener("click", function(){
    var interest_tag = document.getElementsByName("interest_tag");
    var interest_all = document.getElementById("interest_all").firstElementChild.firstElementChild
    if(!interest_all.checked){
        interest_all.checked = true;
        for(var i=1; i<interest_tag.length; i++){
            interest_tag[i].checked = false;
        }
    } else {
        interest_all.checked = false;
    }

});
document.getElementsByName("interest_tag").forEach(function(item){
    item.addEventListener("click", function(){
        var interest_all = document.getElementById("interest_all").firstElementChild.firstElementChild;
        if(item.checked==true && interest_all.checked==true){
            interest_all.checked = false;
        }
    });
});

document.getElementById("agency_all").addEventListener("click", function(){
    var interest_tag = document.getElementsByName("agency_tag");
    var interest_all = document.getElementById("agency_all").firstElementChild.firstElementChild
    if(!interest_all.checked){
        interest_all.checked = true;
        for(var i=1; i<interest_tag.length; i++){
            interest_tag[i].checked = false;
        }
    } else {
        interest_all.checked = false;
    }

});
document.getElementsByName("agency_tag").forEach(function(item){
    item.addEventListener("click", function(){
        var interest_all = document.getElementById("agency_all").firstElementChild.firstElementChild;
        if(item.checked==true && interest_all.checked==true){
            interest_all.checked = false;
        }
    });
});