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
	background-color:#222;
}

div.led.red
{
	background-color:#f00;
}
div.led.green
{
	background-color:#0f0;
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
<div id="box">
	<?php
	for($i = 0; $i < 40; $i++)
	{
		echo('<div class="led" id="led'.$i.'"></div>');
	}
	?>
</div>

<script>

var aSnake = [19, 20];
var iDirection = 1; // 1 = right, 2 = bottom, 3 = left, 4 = top
var iCandy = false;

var aRightBorder = [7, 15, 23, 31, 39];
var aLeftBorder = [0, 8, 16, 24, 32];

var iInterval = false;

$(document).ready(function()
{
	placeNewCandy();

	iInterval = setInterval(function()
	{
		moveSnake();
		displaySnakeAndCandy();
	}, 700);

	$(document).keyup(function(e)
	{
		if(e.keyCode == 37 && iDirection != 1) iDirection = 3;
		if(e.keyCode == 38 && iDirection != 2) iDirection = 4;
		if(e.keyCode == 39 && iDirection != 3) iDirection = 1;
		if(e.keyCode == 40 && iDirection != 4) iDirection = 2;
	});
});

function placeNewCandy()
{
	var iPos = Math.round(Math.random() * 39);
	if(aSnake.indexOf(iPos) != -1)
	{
		placeNewCandy();
		return;
	}

	iCandy = iPos;
}

function moveSnake()
{
	var iHead = aSnake[(aSnake.length -1)];
	switch(iDirection)
	{
		case 1:
			if(isPosFree(iHead + 1) == false || aRightBorder.indexOf(iHead) != -1)
			{
				dieSnakeDIE();
				return;
			}

			aSnake.push(iHead + 1);
			break;
		case 2:
			var iNewPos = iHead + 8;
			if(iNewPos > 39 || isPosFree(iNewPos) == false)
			{
				dieSnakeDIE();
				return;
			}

			aSnake.push(iNewPos);
			break;
		case 3:
			if(isPosFree(iHead - 1) == false || aLeftBorder.indexOf(iHead) != -1)
			{
				dieSnakeDIE();
				return;
			}

			aSnake.push(iHead - 1);
			break;
		case 4:
			var iNewPos = iHead - 8;
			if(iNewPos < 0 || isPosFree(iNewPos) == false)
			{
				dieSnakeDIE();
				return;
			}

			aSnake.push(iNewPos);
			break;
	}

	var iHead = aSnake[(aSnake.length -1)];
	if(iHead == iCandy)
	{
		placeNewCandy();
		return;
	}

	aSnake.shift();
}

function isPosFree(iPos)
{
	if(aSnake.indexOf(iPos) != -1) return false;
	return true;
}

function displaySnakeAndCandy()
{
	$("#box .led").removeClass("red").removeClass("green");
	for(var i in aSnake)
	{
		var iPos = aSnake[i];
		$("#led"+iPos).addClass("red");
	}

	$("#led"+iCandy).addClass("green");
}

function dieSnakeDIE()
{
	clearTimeout(iInterval);
	alert('Game over!');
}

</script>

</body>
<html>
