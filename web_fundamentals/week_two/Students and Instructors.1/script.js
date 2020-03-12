function codingStudents(){
var students ={};
var students= [ 
  {first_name:  'Michael', last_name : 'Jordan'},
  {first_name : 'John', last_name : 'Rosales'},
  {first_name : 'Mark', last_name : 'Guillen'},
  {first_name : 'KB', last_name : 'Tonel'}
];
for(var i=0; i<students.length; i++){
  console.log(students[i].first_name, students[i].last_name);
}
}
codingStudents();

function studentsandinstructors () {
  console.log ('OPTIONAL SOLUTION');
  var users = {
      Students: [
          {first_name: 'Michael', last_name: 'Jordan'},
          {first_name: 'John', last_name: 'Rosales'},
          {first_name: 'Mark', last_name: 'Guillen'},
          {first_name: 'KB', last_name: 'Tonel'}
      ],
      Instructors: [
          {first_name: 'Michael', last_name: 'Choi'},
          {first_name: 'Martin', last_name: 'Puryear'}
      ]
  }
  for (var prop in users) {
      console.log (' ');
      console.log (prop);
      var listnr = 0;
      var fullnamelength = 0;
      for (var i = 0; i < users[prop].length; i++) {
          listnr = i + 1;
          fullnamelength = users[prop][i].first_name.length + users[prop][i].last_name.length;
          console.log (i+1 + ' - ' + users[prop][i].first_name.toUpperCase () + ' ' + users[prop][i].last_name.toUpperCase () + ' - ' + fullnamelength);
      }
  }
}
studentsandinstructors ();