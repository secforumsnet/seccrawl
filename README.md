# seccrawl
<h1>Web Crawler</h1>

<p>This Python script is a versatile web crawler designed to explore and crawl web pages, recording visited URLs and their depths. It provides colorful and stylish output, handles various exceptions gracefully, and can be configured for different crawling depths.</p>

<h2>Features</h2>

<ul>
  <li>Web crawling with specified maximum depth.</li>
  <li>Stylish and colorful command-line interface.</li>
  <li>Exception handling for failed requests and keyboard interrupts.</li>
  <li>Export results to a CSV file.</li>
</ul>

<h2>Requirements</h2>

<p>Before running the script, you need to install the following Python libraries using pip:</p>

<ul>
  <li><b>requests:</b> This library is used for making HTTP requests to web pages.</li>
  <li><b>BeautifulSoup:</b> BeautifulSoup is used for parsing HTML and extracting URLs from web pages.</li>
  <li><b>csv:</b> This library is used for exporting results to a CSV file.</li>
  <li><b>pystyle:</b> Pystyle is used to add stylish and colorful formatting to the command-line interface.</li>
</ul>

<h3>Installation</h3>

<p>Install the required libraries using the following command:</p>

<pre><code>pip install requests beautifulsoup4 csv pystyle</code></pre>

<h2>How to Use</h2>

<ol>
  <li>Clone or download this repository to your local machine.</li>
  <li>Open your terminal or command prompt.</li>
  <li>Navigate to the directory where the script is located.</li>
  <li>Run the script by executing the following command:</li>
</ol>

<pre><code>python seccrawl.py</code></pre>

<li>Follow the on-screen prompts:</li>

<ul>
  <li>Enter the target URL to start crawling from.</li>
  <li>Specify the maximum depth for crawling (e.g., 3).</li>
  <li>Optionally, provide an output file name (e.g., results.json) to save the visited URLs.</li>
</ul>

<li>The script will start crawling the website, recording visited URLs, and saving the results to the specified output file.</li>

</html>
