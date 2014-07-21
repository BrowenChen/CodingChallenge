/*
Automates and converts .md file into jade.
Git Commit to add new jade file into github
Uses fs, markx, html2jade

*/

var fs = require('fs');
var markx = require('markx');
var html2jade = require('html2jade');


var file = "testfile.md"; //This is the name of the md file to be converted to jade
mdFile = fs.readFileSync(file);

var wstream = fs.createWriteStream('testfile.jade'); //Name of jade output file




markx({
    input: 'testMd.md', //can be either a filepath or a source string
    // template: 'layout.html', //can either be filepath or source string
    highlight: true, //parse code snippets for syntax highlighters, default: true
    data: {} //data that gets passed into template
}, function(err, html) {

	html2jade.convertHtml(html, {}, function (err, jade) {
	  
		wstream.on('finish', function () {
		  console.log('file has been written');
		});
		wstream.write(jade);

		wstream.end();			

	});

});

