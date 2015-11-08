function alertM(str){
	alert(str);
}

function algoCheckboxControl(){
	
	var i, j;
	var che = document.getElementsByName("algoCheck");
	var panel = document.getElementsByName("algoShow");

	//check the number of 'ischecked=true'
	if(document.querySelectorAll('input[name="algoCheck"]:checked').length > 2){
		for(i=0;i< che.length ;i++){
			che[i].checked = false;
		}
		for(i=0;i< 3; i++){
			panel[i].innerHTML="&nbsp;";
		}
		alert("알고리즘은 두 개만 선택하시죠?");
	}else{
		//set panel
		j=0;
		
		for(i=0;i<3;i++){
			if(che[i].checked) {
				panel[j].innerHTML = document.getElementById(che[i].getAttribute("id")+"Label").innerHTML;
				j++;
			}
		}
		for(;j<2;j++){
			panel[j].innerHTML="&nbsp;";
		}
	}
}

function sensorCheckboxControl(){
	
	var i, j;
	var che = document.getElementsByName("sensorCheck");
	var panel = document.getElementsByName("sensorShow");

	//check the number of 'ischecked=true'
	if(document.querySelectorAll('input[name="sensorCheck"]:checked').length > 1){
		for(i=0;i< che.length ;i++){
			che[i].checked = false;
		}
		panel[0].innerHTML="&nbsp;";
		alert("센서는 하나만 선택하시죠?");
	}else{
		//set panel
		j=0;
		for(i=0;i<3;i++){
			if(che[i].checked) {
				panel[j].innerHTML = document.getElementById(che[i].getAttribute("id")+"Label").innerHTML;
				j++;
			}
		}
		for(;j<2;j++){
			panel[j].innerHTML="&nbsp;";
		}
	}
}






// 여기서부터 morris chart

// function getXMLHttpRequest(url_param, callback){
// 	var httpRequest;
// 	httpRequest = new XMLHttpRequest();
// 	return(function(ajax, method, url, callback){
// 		var url = url;
// 		httpRequest.onreadystatechage = function(){
// 			if(httpRequest.status === 200 && httpRequest.readyState === 4){
// 				eval(callback)(httpRequest);
// 			}
// 		};

// 		httpRequest.open(method, url, true);
// 		httpRequest.send(null);
// 	})(httpRequest, 'GET', url_param, callback);
// }

// function responseRecv_Method(res){
// 	console.log(res.responseText);
// }

// setTimeout(function(){
// 	getXMLHttpRequest("/morris_data", responseRecv_Method);
// }, 1000);



//new
$(function () {
  eval($('#code').text());
});

