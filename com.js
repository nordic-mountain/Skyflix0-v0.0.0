// your_script.js
document.addEventListener("DOMContentLoaded", function () {
    var script = document.createElement('script');
    script.src = 'data.js';
    script.onload = function() {
        console.log(pythonData);  // Access the Python data in the browser's console
    };
    document.head.appendChild(script);
});

