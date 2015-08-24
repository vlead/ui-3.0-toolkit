function evaluate()
{
	var form = document.forms["quiz"];

	/* Initialise qnswers */
	var a1a = "(2, 2)";
	var a1b = "(-2, 3)";
	var a1c = "(-4, 0)";
	var a1d = "(-3, -3)";
	var a1e = "(4, -3)";
	var a2  = "1";
	var a3  = "3";

	/* Extract answers */
	var q1a = form["q1_a"].value;
	var q1b = form["q1_b"].value;
	var q1c = form["q1_c"].value;
	var q1d = form["q1_d"].value;
	var q1e = form["q1_e"].value;
	var q2, q3, length;
	
	length = form["q2"].length;
	for(i=0; i<length; i++)
		if(form["q2"][i].checked)
			q2 = form["q2"][i].value;
	
	length = form["q3"].length;
	for(i=0; i<length; i++)
		if(form["q3"][i].checked)
			q3 = form["q3"][i].value;

	/* Evaluate answers */
	var score = 0;
	var result = "";

	if(q1a == a1a)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q1a</font>, ";

	if(q1b == a1b)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q1b</font>, ";

	if(q1c == a1c)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q1c</font>, ";

	if(q1d == a1d)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q1d</font>, ";

	if(q1e == a1e)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q1e</font>, ";

	if(q2 == a2)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q2</font>, ";

	if(q3 == a3)
	{
		score++;
		result += "<font color='red'>";
	}
	else
		result += "<font color='green'>";
	result += "Q3</font>";


	/* Show result */
	var output = "Your score is " + score + "\n";
	output += result;
	
	alert(output);
	return false;
}
