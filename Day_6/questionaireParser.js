module.exports = {
    parseQuestionaires: function (inputString) {
        var inputSplitOnNewLine = inputString.split('\n');
        var groups = this.coalesceToGroups(inputSplitOnNewLine);
        var count = 0;

        for(let group of groups) {
            count = count + this.calculateGroupCount(group);
        }

        console.log(groups);
        return count;
    },
    coalesceToGroups: function(listOfInputLines) {
        let collectedAnswers = []
        let groupAnswer = '';
        let countOfPeopleInGroup = 0;
        for(let line of listOfInputLines) {
            if(line === '') {
                collectedAnswers.push({
                    count: countOfPeopleInGroup,
                    answers: groupAnswer});
                groupAnswer = '';
                countOfPeopleInGroup = 0;
            }
            else {
                countOfPeopleInGroup = countOfPeopleInGroup + 1;
                groupAnswer = groupAnswer + line;
            }
        }
        return collectedAnswers;
    },
    calculateGroupCount: function(group) {
        let alphabet = 'qwertyuiopasdfghjklzxcvbnm';
        let count = 0;
        for(let char of alphabet) {
            let countOfCharInGroup = (group.answers.match(new RegExp(char, "g")) || []).length;
            if(countOfCharInGroup == group.count){
                count = count + 1;
            }
        }
        return count;
    }

}