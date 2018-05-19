// Define SVG area dimensions
var svgWidth = 800;
var svgHeight = 500;

// Define the chart's margins as an object
var chartMargin = {
  top: 50,
  right: 50,
  bottom: 50,
  left: 50
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select(".chart")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth)
  .append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Append a group to the SVG area
var chart = svg.append("g");

//Append a div to the chart to create tooltips, and assign it a class.
d3.select(".chart")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 1);

// Load data from the csv file
d3.csv("data/data.csv", function (error, myData) {

  // Log an error if one exists
  if (error) return console.warn(error);

  // Print the data
  console.log(myData);

  // Cast the values to a number for each piece of myData
  myData.forEach(function (data) {
    data.below_poverty =+data.below_poverty;
    data.no_healthcare =+data.no_healthcare;
  });

  // Create x and y scale functions
  var xScale = d3.scaleLinear().range([0, chartWidth]);
  var yScale = d3.scaleLinear().range([chartHeight,0]);

  var bottomAxis = d3.axisBottom(xScale);
  var leftAxis = d3.axisLeft(yScale);

  //Scale the domain
	xScale.domain([0, d3.max(myData, function(data){
		return +data.below_poverty;
	})]);

	yScale.domain([0, d3.max(myData,function(data){
		return +data.no_healthcare;
  })]);

  var xMin = d3.min(myData, function(d) {return +d.below_poverty * 0.9;});
  var xMax = d3.max(myData, function(d) {return +d.below_poverty * 1.1;});
  var yMin = d3.min(myData, function(d) {return +d.no_healthcare * 0.9;});
  var yMax = d3.max(myData, function(d) {return +d.no_healthcare *1.1;});

  xScale.domain([xMin, xMax]);
  yScale.domain([yMin, yMax]);

  // Initialize tooltip 
  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([0, -20])
    .html(function(data) {
        var state = data.State;
        var poverty = +data.below_poverty;
        var hcare = +data.no_healthcare;
        return (
            state + '<br> poverty: ' + poverty + '% <br> uninsured: ' + hcare +'%'
        );
  });

// Create tooltip
chart.call(toolTip);

chart.selectAll("circle")
  .data(myData)
  .enter()
  .append("circle")
  .attr("cx", function(d, i) {
      return xScale(d.below_poverty);
  })
  .attr("cy", function(d, i) {
      return yScale(d.no_healthcare);
  })
  .attr("r", "12")
  .attr("fill", "lightblue")
  .style("opacity", 0.8)
  
  // display tooltip on mouseover
  .on("mouseover", function(d) {
      toolTip.show(d);
  })
  // hide tooltip on mouseout
  .on("mouseout", function(d) {
      toolTip.hide(d);
  });

  // bind data and append text to create labels for each data points
  chart.selectAll("g")
    .data(myData)
    .enter()
    .append("text")
    .attr("dx", function(d, i){
      return xScale(d.below_poverty);
    })
    .attr("dy", function(d, i){
      return yScale(d.no_healthcare);
    })
    .text(function (d, i){
      return d.StateAbbr;
    });

  // call x and y axis
  chart.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(bottomAxis);

  chart.append("g")
      .call(leftAxis);

  // x-axis labels
  chart.append("text")
    .attr("transform", "translate(" + (chartWidth / 2) + " ," + (chartHeight + chartMargin.top-10) + ")")
    .attr("class", "xlabel")
    .text("In Poverty (%)");

  // y-axis labels
  chart.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - chartMargin.left)
    .attr("x", 0 - (chartHeight / 2))
    .attr("dy", "1em")
    .attr("class", "ylabel")
    .text("No Healthcare (%)");  
});

