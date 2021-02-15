# AutoCrack
AutoCrack is a crypto bruteforcer for CTFs.
It is designed based on the principle of finding keyword of flags from encoded messages.
AutoCrack currently supports the vigenere cipher and the caesar cipher.


<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>



<h2>How it works:</h2>
<h3>Caesar:</h3>
<list>
  <ol>encode the keyword by rot <i>num</i></ol>
  <ol>return if encoded keyword is in message</ol>
  <ol>repeat</ol>
</list>
<h3>Vigenere:</h3>
<list>
  <ol>decode the message with key <i>num</i></ol>
  <ol>return if keyword is in decoded message</ol>
  <ol>repeat</ol>
</list>
<h2>How to use:</h2>
<h3>Caesar (case-insensitive) :</h3>
autoCaesar(message, keyword)
<h3>Vigenere (case-insensitive) :</h3>
autoVigenere(message, keyword, min=2, max=5)
