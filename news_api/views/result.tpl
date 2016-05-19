<!DOCTYPE html>
<html>

<head>
<title>Results</title>
</head>

<body>
<h3>Number of results</h3> {{counts}}
<h3>Results:</h3><br> 
<ol>
%for r in results:
<li><p>
<ul>
    <li>{{r['title']}}</li>
    
</ul>

</p></li>
%end
</ol>
</body>

</html>
