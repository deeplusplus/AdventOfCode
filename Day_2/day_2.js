var fs = require("fs");

let lineObjects = [];
let lineStrings = [];
let lineAsList = '';
let validPwdCount = 0;
let charCount = 0;

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
            charCount = (lineObject.pwd.match(new RegExp(lineObject.keyChar.charAt(0), "g")) || []).length;
            if (charCount >= lineObject.charMin && charCount <= lineObject.charMax) {
                validPwdCount = validPwdCount + 1;
            }
        }
    }
    console.log(validPwdCount);
});