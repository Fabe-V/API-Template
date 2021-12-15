$.getJSON("https://01e8-2003-df-ff46-d74c-88d-974-dfcb-8cf4.ngrok.io/",
function(data){
console.log(data);
$('.data_1').append(data.test_number);
$('.data2').append(data.test_zahl);

}
);