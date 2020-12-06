var express = require('express');
var { graphqlHTTP } = require('express-graphql');
var { buildSchema } = require('graphql');
var app = express();
var path = require('path');
var router = express.Router();
var parser = require('./questionaireParser.js')

app.use(express.static(__dirname + '/src'));

router.get('/', function(req, res) {
    res.sendFile(path.join(__dirname+'/src/dataInput.html'));
});

var schema = buildSchema(`
    type Query { 
        processData(data: String!): String
    }
`);

var root = {
    processData: (queryObject) => {
        let answer = parser.parseQuestionaires(queryObject.data);
        return `THE RETURNED VALUE IS ${answer}`;
    },
};

app.use('/graphql', graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
}));


app.listen(3000);
app.use('/', router);
console.log('Running server and GraphQL api at localhost:3000')