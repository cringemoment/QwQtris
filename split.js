const {decoder, encoder} = require('tetris-fumen');

// Get the fumen from the command line
const fumenString = process.argv[2];

// Parse the fumen into a Fumen object
const f = decoder.decode(fumenString);

f.forEach((field) => {
  field = field.field.str();
  fieldRows = field.split('\n');
  fieldRows.pop();
  field = fieldRows.join('');
  page = {
    field: field,
  };

  // Encode the page to Fumen
  fumen = encoder.encode([page]);

  console.log(fumen);
})
