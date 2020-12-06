var express = require('express');
var { graphqlHTTP } = require('express-graphql');
var { buildSchema } = require('graphql');
var app = express();
var path = require('path');
var router = express.Router();

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
    processData: (data) => {
        console.log(data);
        return "THIS IS THE RETURNED VALUE";
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