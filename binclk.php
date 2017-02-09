<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Pleh</title>
<style>

body
{
	background-color:#000;
	margin:0px;
}

div.led
{
	float:left;
	border:1px solid #333;
	border-radius:100%;
	width:20px;
	height:20px;
	margin-right:5px;
	margin-bottom:5px;
	background-color:#400;
}

div.led.on
{
	background-color:#f00;
}

#box
{
	width:216px;
	height:200px;
	margin:100px auto 0px auto;
}

</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</head>
<body>

<!--

PHP, HTML, Javascript & jQuery version of a binary clock
(c) 2017 Bas van der Sluis

-->

<div id="box">
	<?php
	for($i = 0; $i < 40; $i++)
	{
		echo('<div class="led" id="led'.$i.'"></div>');
	}
	?>
</div>

<script>

// 1 = first column
var iStartColumn = 1;
var bSpace = true;

$(document).ready(function()
{
	displayTime();

	setInterval('displayTime()', 1000);
});

function displayTime()
{
	var oDate = new Date();
	var sHours = String(oDate.getHours());
	var sMinutes = String(oDate.getMinutes());
	var sSeconds = String(oDate.getSeconds());

	displayNumber(iStartColumn, sHours);

	var iColumnAdd = 2;
	if(bSpace) iColumnAdd = 3;

	displayNumber(iStartColumn + iColumnAdd, sMinutes);

	var iColumnAdd = 4;
	if(bSpace) iColumnAdd = 6;

	displayNumber(iStartColumn + iColumnAdd, sSeconds);
}

function displayNumber(iColumn, sNumber)
{
	if(sNumber.length == 1)
	{
		displayColumn(iColumn, 0);
		displayColumn(iColumn + 1, parseInt(sNumber));
	}
	else
	{
		displayColumn(iColumn, parseInt(sNumber.substring(0, 1)));
		displayColumn(iColumn + 1, parseInt(sNumber.substring(1, 2)));
	}
}

function displayColumn(iColumn, iDigit)
{
	var iPos = 32 + (iColumn - 1);

	for(var b = 1; b <= 16; b *= 2)
	{
		if(iDigit & b)
			$("#led"+iPos).addClass("on");
		else
			$("#led"+iPos).removeClass("on");

		iPos -= 8;
	}
}

</script>

</body>
<html>
