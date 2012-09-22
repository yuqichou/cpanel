function customShowErrors() {
	
	var t = this;
	
	for (var i = 0; this.errorList[i]; i++) {
		var error = this.errorList[i];
		var message = error.message;
		var element = error.element;
		
		$(element).css("border", "solid 1.5px red");
		$(element).attr("errorMessage",message);
		
//		$(element).mouseover(function(e) {
//					var tooltip = "<div id='tooltip'><p id='tooltipMessage'></p></div>";
//					if(!document.getElementById('tooltip')){
//						$('body').append(tooltip);
//					}
//					$("#tooltipMessage").html(e.target.getAttribute("errorMessage"));
//					$('#tooltip').css({"opacity" : "0.8",
//										   "top" : (e.pageY + 20) + "px",
//										  "left" : (e.pageX + 10) + "px"
//									}).show('fast');
//				});
//		$(element).mouseout(function() {
//					$('#tooltip').remove();
//		});
//		$(element).mousemove(function(e) {
//				$('#tooltip').css({"top" : (e.pageY + 20) + "px",
//								  "left" : (e.pageX + 10) + "px"});
//		});
		
		
	}
	
	for(var j=0;j<this.successList.length;j++){
		$(this.successList[j]).css("border", "solid 1px green");
		$(this.successList[j]).attr("errorMessage","");
//		$(this.successList[j]).unbind("mouseover");
//		$(this.successList[j]).unbind("mouseout");
//		$(this.successList[j]).unbind("mousemove");
	}
}


// cn
jQuery.extend(jQuery.validator.messages, {   
        required: "必选字段",   
        remote: "请修正该字段",   
        email: "请输入正确格式的电子邮件",   
        url: "请输入合法的网址",   
        date: "请输入合法的日期",   
        dateISO: "请输入合法的日期 (ISO).",   
        number: "请输入合法的数字",   
        digits: "只能输入整数",   
        creditcard: "请输入合法的信用卡号",   
        equalTo: "请再次输入相同的值",   
        accept: "请输入拥有合法后缀名的字符串",   
        maxlength: jQuery.validator.format("请输入一个长度最多是 {0} 的字符串"),   
        minlength: jQuery.validator.format("请输入一个长度最少是 {0} 的字符串"),   
        rangelength: jQuery.validator.format("请输入一个长度介于 {0} 和 {1} 之间的字符串"),   
        range: jQuery.validator.format("请输入一个介于 {0} 和 {1} 之间的值"),   
        max: jQuery.validator.format("请输入一个最大为 {0} 的值"),   
        min: jQuery.validator.format("请输入一个最小为 {0} 的值")   
});  


/**
 * 为空元素赋name值
 */
function assignNameForNull(){
	var ms=new Date().getMilliseconds();
	for(var i in $.validator.methods){
		$('.'+i).each(function(){
			if($(this).is(":visible")){	//隐藏元素不判断
				if(this.name<1){
					this.name="tempName_"+(ms++);
				}
			}
		});
	}
}





