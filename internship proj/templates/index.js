document.getElementById("secSet").style.display = "none";
document.getElementById("finals").style.display = "none";

$("#firstButton").click(function(){
  var checkedValue = $('.form-check-input:checked').val();
  if(checkedValue == undefined){
    alert("choose a salary >:(")
  }else{
    document.getElementById("firstSet").style.display = "none";
    $("#secSet").show();
  }
});

$("#secondButton").click(function(){
  var checkedValue = $('.form-check-input:checked').val();
  var secChoices = [];
        $(':checkbox:checked').each(function(i){
          secChoices[i] = $(this).val();
        });
        finalVal = [checkedValue, secChoices]
        alert("Second choice values are " +  finalVal);
        document.getElementById("secSet").style.display = "none";
        $("#finals").show();
        $.getJSON("data.json", function(data){
        console.log(data);
      })
})
