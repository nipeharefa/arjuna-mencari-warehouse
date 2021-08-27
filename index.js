const CheapRuler = require('cheap-ruler');
var ruler = new CheapRuler(50.5, 'meters'); // calculations around latitude 35

// const my = [-6.213797, 106.820238];
const mandiri = [-6.214249, 106.819840];
const wtc = [-6.214126, 106.819716];
const mcc = [-6.215935, 106.818241];
const medan = [3.5952, 98.672226]
const bukitTinggi = [-0.3039, 100.3835]

const datas = [bukitTinggi,mandiri, wtc, medan];


datas.forEach(x => {

	const distance = ruler.distance(mcc, x);
	console.log(distance);
});
