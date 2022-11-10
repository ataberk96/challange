


data = '<url>https://xcd32112.smart_meter.com</url> '
if data[:13] == '<url>https://':
    print(data[13:-7])
if data[:12] == '<url>http://':
    print(data[12:-7]) 
