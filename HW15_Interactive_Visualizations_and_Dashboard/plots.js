var $selDataset = document.getElementById("selDataset")
var $pie = document.getElementById("pie")
var $bubble = document.getElementById("bubble")

function getSampleNames() {
  /* data route */
  var url = "/names";
  Plotly.d3.json(url, function(error, response) {

    console.log(response);

    var data = [response]

    for (var i=0; i<data.length; i++)  {
      var $option = document.createElement("option");
      $option.setAttribute("value", data[i]);
      $option.innerHTML = data[i];

      $selDataset.appendChild($option);
    };
  });  
