const calorieCounter = document.getElementById('calorie-counter');
const budgetNumberInput = document.getElementById('budget');
const entryDropdown = document.getElementById('entry-dropdown');
const addEntryButton = document.getElementById('add-entry');
const clearButton = document.getElementById('clear');
const output = document.getElementById('output');
let isError = false;

function cleanInputString(str) {
    // test - console.log("original string: ", str) 
    const regex = /[+-\s]/g; // +, -, spaces, whitespace in character class
    return str.replace(regex,"");  
    // test - console.log(cleanInputString("+-99")) 
  }

function isInvalidInput(str) {
    const regex = /\d+e\d+/i;
    return str.match(regex);
    // test console.log(isInvalidInput("10"));

  }

function addEntry() {

  }  