// let timestamp = 637776829355875500 % 10 ** 8;
// let timestamp = 637776829355875500;
// console.log(timestamp);

// function timeConverter(timestamp) {
//   var a = new Date(timestamp * 1000);
//   var months = [
//     'Jan',
//     'Feb',
//     'Mar',
//     'Apr',
//     'May',
//     'Jun',
//     'Jul',
//     'Aug',
//     'Sep',
//     'Oct',
//     'Nov',
//     'Dec'
//   ];
//   var year = a.getFullYear();
//   var month = months[a.getMonth()];
//   var date = a.getDate();
//   var hour = a.getHours();
//   var min = a.getMinutes();
//   var sec = a.getSeconds();
//   var time =
//     date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec;
//   return time;
// }

// console.log(timeConverter(timestamp));
let timestamp = 637776829355875500 / 10 ** 6;
console.log(timestamp);
var date = new Date(timestamp);
console.log(date.getTime());
console.log(date);
