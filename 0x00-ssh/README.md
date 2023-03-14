<link rel="stylesheet" type="text/css" href="styles/0-README.css">

<img src="https://user-images.githubusercontent.com/105602291/224162963-3d1a36dc-ab21-4b02-9051-e4a74db80074.png" style="display: black; margin: auto;"/><hr/>

<h1>0x00. SSH (README not finished) &#x1F4F6</h1>
    <h2>Resources &#x1F4DA</h2>
        <p><b>Read or watch:</b></p>
        <ul class="resources">
            <li><a href="https://docs.python.org/3/howto/urllib2.html">Quickstart with Requests package</a></li>
            <li><a href="https://docs.python-requests.org/en/latest/">Requests package</a></li>
        </ul>
    <hr/>
    <h2>Learning Objectives &#x1F4A1;</h2>
        <h3>General</h3>
            <ul class="learn">
                <li>How to fetch internet resources with the Python package <span>urllib</span></li>
                <li>How to decode <span>urllib</span> body response</li>
                <li>How to use the Python package <span>requests</span> #requestsiswaysimplerthanurllib</li>
                <li>How to make HTTP <span>GET</span> request</li>
                <li>How to make HTTP <span>POST</span>/<span>PUT</span>/etc. request</li>
                <li>How to fetch JSON resources</li>
                <li>How to manipulate data from an external service</li>
            </ul>
    <hr/>
    <h2>Requirements</h2>
        <h3>General</h3>
            <ul class="required">
                <li>Allowed editors: <span>vi</span>, <span>vim</span>, <span>emacs</span></li>
                <li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <span>python3</span> (version 3.4.3)</li>
                <li>All your files should end with a new line</li>
                <li>The first line of all your files should be exactly <span>#!/usr/bin/python3</span></li>
                <li>A <span>README.md</span> file, at the root of the folder of the project, is mandatory</li>
                <li>Your code should use the <span>PEP 8</span> style (version 1.7)</li>
                <li>All your files must be executable</li>
                <li>The length of your files will be tested using <span>wc</span></li>
                <li>All your modules should have a documentation (<span>python3 -c 'print(__import__("my_module").__doc__)'</span>)</li>
                <li>You must use <a href="https://docs.python.org/3.4/library/stdtypes.html#dict.get">get</a> to access the dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)</li>
                <li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
                <li>Your code should not be executed when imported (by using <span>if __name__ == "__main__":</span>)</li>
            </ul>
    <hr/>
    <section class="tasks">
        <h3>0. What's my status? #0</h3>
            <ul>
                <li>Write a Python script that fetches https://intranet.hbtn.io/status</li>
            </ul>
        <h3>1. Response header value #0</h3>
            <ul>
                <li>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.</li>
            </ul>
        <h3>2. POST an email #0</h3>
            <ul>
                <li>Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).</li>
            </ul>
        <h3>3. Error code #0</h3>
            <ul>
                <li>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).</li>
            </ul>
        <h3>4. What's my status? #1</h3>
            <ul>
                <li>Write a Python script that fetches https://intranet.hbtn.io/status</li>
            </ul>
        <h3>5. Response header value #1</h3>
            <ul>
                <li>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header</li>
            </ul>
        <h3>6. POST an email #1</h3>
            <ul>
                <li>Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.</li>
            </ul>
        <h3>7. Error code #1</h3>
            <ul>
                <li>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.</li>
            </ul>
        <h3>8. Search API</h3>
            <ul>
                <li>Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.</li>
            </ul>
        <h3>9. My Github!</h3>
            <ul>
                <li>Write a Python script that takes your Github credentials (username and password) and uses the Github API to display your id</li>
            </ul>
    </section>
    <hr/>
    <h3>Authors</h3>
        <ul class="authors">
            <li> Foster Clark - <a href="https://github.com/FosterClark48">fozc</a></li>
        </ul>
