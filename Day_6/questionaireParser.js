module.exports = {
    parseQuestionaires: function (inputString) {
        var inputSplitOnNewLine = inputString.split('\n');
        var groupedAnswers = this.coalesceToGroups(inputSplitOnNewLine);
        var count = 0;

        for(let answer of groupedAnswers) {
            count = count + this.calculateGroupCount(answer);
        }

        return count;
    },
    coalesceToGroups: function(listOfInputLines) {
        let collectedAnswers = []
        let groupsAnswers = '';
        for(let line of listOfInputLines) {
            if(line === '') {
                collectedAnswers.push(groupsAnswers);
                groupsAnswers = '';
            }
            else {
                groupsAnswers = groupsAnswers + line;
            }
        }
        return collectedAnswers;
    },
    calculateGroupCount: function(groupAnswer) {
        let groupSet = new Set();
        for(let char of groupAnswer) {
            groupSet.add(char);
        }
        return groupSet.size;
    }

}