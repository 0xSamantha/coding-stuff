const character = "Hello";
const count = 8;
const rows = [];
for (let i = 0; i < count; i = i + 1) {
    rows.push(character);
  character.repeat(i);
  }
  
  let result = ""

for (const row of rows) {
    result = result + row;
  }