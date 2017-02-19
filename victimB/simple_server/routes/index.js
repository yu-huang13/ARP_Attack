var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/sign_in', function(req, res){
	res.send('sign in successfully!\n');
});

module.exports = router;
