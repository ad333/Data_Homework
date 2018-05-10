// var $selDataset = document.getElementById("selDataset");
// var $pie = document.getElementById("pie");
// var $bubble = document.getElementById("bubble");
// var $metadata = document.getElementById("metadata");


function getSampleNames() {
  var x = [];
  
  // data route 
  var url = "/names";
  Plotly.d3.json(url, function(error, response) {

    if (error) return console.warn(error);
    
    for (i=0; i<response.length; i++)  {
      x.push(response[i]);
    
      var opt = document.createElement("option");        
      var t = document.createTextNode(x[i]);     
      opt.appendChild(t);                               
      document.getElementById("selDataset").appendChild(opt);
    }
    //console.log(x);
    return x;
  })
}; 
getSampleNames(); 


function init(sample = "BB_940")  {
  plotBubble(sample);
  displayMetadata(sample);
  plotPie(sample);
};


function optionChanged(sample)  {
  plotPie(sample);
  plotBubble(sample);
  displayMetadata(sample);
};

// optionChanged(sample);

function plotPie(sample)  {
  var url = "/samples/" + sample;
  Plotly.d3.json(url, function(error, response)  {
    if (error) return console.warn(error);

    var labels_list = [];
    var values_list = [];
    /*
    for (i=0; i<10; i++)  {
      var label = response["otu_ids"][i];
      labels_list.push(label);
      var value = response["sample_values"][i];
      values_list.push(value);
    };
    */

    var labels_list = response["otu_ids"].slice(0, 10);
    var values_list = response["sample_values"].slice(0, 10);

    var trace1 = {
      labels: labels_list,
      values: values_list,
      type: "pie"
    };
    
    var data = [trace1];
    
    var layout = {
      title: "'Pie' Chart",
      xaxis: {title: 'otu_ids'},
      yaxis: {title: 'sample_values'}
    };
    
    Plotly.newPlot("pie", data, layout);
  });
};


function plotBubble(sample)  {
  var url = "/samples/" + sample;
  Plotly.d3.json(url, function(error, response)  {
    if (error) return console.warn(error);
    
    var labels_list = [];
    var values_list = [];

    var labels_list = response["otu_ids"].slice(0, 10);
    var values_list = response["sample_values"].slice(0, 10);

    var trace1 = {
      labels: labels_list,
      values: values_list,
      type: "bubble"
    };
    
    var data = [trace1];
    
    var layout = {
      title: "'Bubble' Chart",
      xaxis: {title: 'otu_ids'},
      yaxis: {title: 'sample_values'}
    };
    
    Plotly.newPlot("bubble", data, layout);
  });
};
 

function displayMetadata(sample)  {
  var url = "/metadata/" + sample;
  Plotly.d3.json(url, function(error, response)  {
    if (error) return console.warn(error);
  console.log(response);
  
  var data = response;
  
  document.getElementById("metadata").innerHTML = data;


  });  
};









