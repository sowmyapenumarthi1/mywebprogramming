<html>
<body>
%if extra != None: 
    <h2>Hello, {{name}}! {{extra}}</h2>
%else:
    <h2>Hello, {{name}}! Have a great day!</h2>
%end
<br>
...from the template!
</body>
</html>