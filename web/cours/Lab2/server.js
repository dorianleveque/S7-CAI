const express = require("express")
//const myData = require('./data.json');
const beerList = require('./assets/beers/beers.json');

const app = express()

//app.use('/img', express.static('assets/img'));
app.use('/beers/img', express.static('assets/img'));  
app.use(express.static('public'));


/*************
    Routes
*************/

app.get('/', (req, res) => {
    console.log('Received request from', req.ip)
    res.send('Hello World!')
})

app.get('/beers', (req, res) => {
    console.log('Received request for beers from', req.ip)
    res.json(beerList);
})
  
app.get('/beer/:beerId', (req, res) => {
    console.log('Received request for '+req.params['beerId']+' from', req.ip)
    let beerDetails = require('./assets/beers/'+req.param('beerId')+'.json');
    res.json(beerDetails);
})


const server = app.listen(3000, () => {
    let host = server.address().address
    let port = server.address().port
    console.log('Listening at http://%s:%s', host, port)
})