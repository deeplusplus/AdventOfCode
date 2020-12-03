var fs = require("fs");

let lineObjects = [];
let lineStrings = [];
let lineAsList = '';
let validPwdCount = 0;

fs.readFile('input1.txt', function (err, data) {
    if (err) {
        return console.error(err);
    }
    lineStrings = data.toString().split("\n");

    for (lineString of lineStrings) {
        lineAsList = lineString.split(" ");
        if (lineAsList.length > 0) {
            lineObjects.push({
                charMin: parseInt(lineAsList[0].split("-")[0]),
                charMax: parseInt(lineAsList[0].split("-")[1]),
                keyChar: lineAsList[1],
                pwd: lineAsList[2]
            });
        }
    }

    for (lineObject of lineObjects) {
        if (lineObject.pwd) {
            let keyChar = lineObject.keyChar.charAt(0);
            let char1 = lineObject.pwd.charAt(lineObject.charMin - 1);
            let char2 = lineObject.pwd.charAt(lineObject.charMax - 1);

            if(char1 === keyChar ^ char2 === keyChar) {
                validPwdCount = validPwdCount + 1;
            }
        }
    }
    console.log(validPwdCount);
});