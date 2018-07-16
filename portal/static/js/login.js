function myFunction() {
    var x = document.getElementById("pass");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


function myfunc() {
	var x = document.getElementById("user");
	var y = document.getElementById("pass");
	
	if(x.value === "9423050" && y.value==="123"){
		location.replace("file:///C:/Users/Mohammad/Desktop/New%20folder/student_course/index.html")
	} else {
		document.getElementById("wrong").style.display="block";
	}
}
