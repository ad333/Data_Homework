// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredData to dataSet initially
var filteredData = dataSet;

// renderTable renders the filteredData to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredData.length; i++) {
    // Get get the current ufo_record object and its fields
    var ufo_record = filteredData[i];
    var fields = Object.keys(ufo_record);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the ufo_record object, create a new cell at set its inner text to be the current value at the current ufo_record's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = ufo_record[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDatetime = $datetimeInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  // Set filteredData to an array of all data whose records matches the filter
  filteredData = dataSet.filter(function(ufo_record) {
    var dataDatetime = ufo_record.datetime.toLowerCase();
    var dataCity = ufo_record.city.toLowerCase();
    var dataState = ufo_record.state.toLowerCase();
    var dataCountry = ufo_record.country.toLowerCase();
    var dataShape = ufo_record.shape.toLowerCase();

    // If true, add the input data to the filteredData, otherwise don't add it to filteredData
    if (filterDatetime)
      return dataDatetime === filterDatetime;
    else if (filterCity)
      return dataCity === filterCity; 
    else if (filterState)
      return dataState === filterState;
    else if (filterCountry)
      return dataCountry === filterCountry;
    else if (filterShape)
      return dataShape === filterShape;  
    else
      return ("");  
  });
  renderTable();
}

// Render the table for the first time on page load
renderTable();

// Pagination
/*
$('#ufotable').dataTable( {
  "pageLength": 50
} );
*/

$(document).ready(function() {
  $('#ufotable').DataTable( {"pageLength":50});
} );



    
