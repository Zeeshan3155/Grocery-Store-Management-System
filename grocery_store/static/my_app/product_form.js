
document.getElementById('closeBtn').addEventListener('click', function() {
    document.getElementById('popupForm').style.display = 'none';
    document.querySelector(".selectAction").value = '';
});

document.getElementById('closeBtn2').addEventListener('click', function() {
    document.getElementById('popupForm2').style.display = 'none';
    document.querySelector(".selectAction").value = '';
});

document.getElementById('closeBtn3').addEventListener('click', function() {
    document.getElementById('popupForm3').style.display = 'none';
    document.querySelector(".selectAction").value = '';
});


$('#pf_edit_product').on('change', function(){
   console.log("This is event");
   const selectedOption = this.options[this.selectedIndex];
   console.log(selectedOption.getAttribute("p_name"));
   document.querySelector('#pf_edit_price').value = selectedOption.getAttribute("p_price");
   document.querySelector('#pf_edit_name').value = selectedOption.getAttribute("p_name");
})


window.onclick = function(event) {
    var modal1 = document.getElementById('popupForm');
    var modal2 = document.getElementById('popupForm2');
    var modal3 = document.getElementById('popupForm3');
    if (event.target == modal1) {
        modal1.style.display = 'none';
        document.querySelector(".selectAction").value = '';
    }else if(event.target == modal2){
        modal2.style.display = 'none';
        document.querySelector(".selectAction").value = '';
    }else if(event.target == modal3){
        modal3.style.display = 'none';
        document.querySelector(".selectAction").value = '';
    }
}

function confirmDelete() {
        // Show confirmation dialog
        if (confirm("Are you sure you want to delete this product?")) {
            // If user confirms, submit the form
            document.getElementById("delete_form").submit();
        }
        // If user cancels, do nothing (form will not be submitted)
    }

document.querySelector(".selectAction").addEventListener('click', function(){
    if (this.value == '1'){
        document.querySelector("#popupForm").style.display = 'block'

    }else if(this.value == '2'){
        document.querySelector("#popupForm2").style.display = 'block'

    }else if(this.value == '3'){
        document.querySelector("#popupForm3").style.display = 'block'

    }
});
