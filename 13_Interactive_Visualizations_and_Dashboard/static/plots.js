// Function to get sample ids/names
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


// Function to get otu descriptions
function getOtuDescriptions()  {
  var url = "/otu";
  Plotly.d3.json(url, function(error, response) {

    if (error) return console.warn(error);
    
    for (i=0; i<response.length; i++)  {
      x.push(response[i]);
    }
    //console.log(x);
    return x;
  })
}


// Function to create initial page using default data (BB_940)
function init(sample)  {
  plotPie(sample);
  plotBubble(sample);
  displayMetadata(sample);
};
init("BB_940");


// Function to handle option change 
function optionChanged(sample)  {
  plotPie(sample);
  plotBubble(sample);
  displayMetadata(sample);
};
// optionChanged(sample);


// Function to create pie chart
function plotPie(sample)  {
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
      hovertext: labels_list,
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


// Function to create bubble chart
function plotBubble(sample)  {
  var url = "/samples/" + sample;
  Plotly.d3.json(url, function(error, response)  {
    if (error) return console.warn(error);
    
    var labels_list = [];
    var values_list = [];

    var labels_list = response["otu_ids"];
    var values_list = response["sample_values"];

    var trace = {
      x: labels_list,
      y: values_list,
      mode: "markers",
      marker:{
        color: labels_list,
        size: values_list,
        mode: "markers",
        text: labels_list,
        type: "scatter"
      }
    }
    
    var data = [trace];
    
    var layout = {
      title: "'Bubble' Chart",
      xaxis: {title: 'otu_ids'},
      yaxis: {title: 'sample_values'}
    }
    
    Plotly.newPlot("bubble", data, layout);
  });
};
 

// Function to display sample metadata info
function displayMetadata(sample)  {
  var url = "/metadata/" + sample;
  Plotly.d3.json(url, function(error, response)  {
    if (error) return console.warn(error);
    console.log(response);
    
    var keys_ = Object.keys(response);
    var values_ = Object.values(response)

    var v = document.getElementById("metadata");
    v.innerHTML = "";
    for (i = 0; i < keys_.length; i++) {
      var par = document.createElement("p");
      par.innerHTML = keys_[i] + ": " + values_[i]; 
      v.appendChild(par)
    }
  });  
};