const words = require('cmu-pronouncing-dictionary')
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 
'october', 'november', 'december']

for (var i=0; i<months.length; i++) {
	console.log(months[i] + ' ' + words[months[i]])
}