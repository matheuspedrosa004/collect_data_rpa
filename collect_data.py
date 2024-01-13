from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.google.com/search?q=d%C3%B3lar+hoje&oq=d%C3%B3lar+hoje&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMgwIARAjGCcYgAQYigUyDQgCEAAYgwEYsQMYgAQyCggDEAAYsQMYgAQyCggEEAAYsQMYgAQyCggFEAAYsQMYgAQyDQgGEAAYgwEYsQMYgAQyBwgHEAAYgAQyCggIEAAYsQMYgAQyCggJEAAYsQMYgATSAQgxMzY0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
    dolar = page.locator('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text_content()
    dolar = dolar.replace(',', '.') 
    print(f'The dolar is coasting R${dolar} brazilian real')

    page.goto("https://www.google.com/search?q=euro+hoje&sca_esv=598210265&sxsrf=ACQVn08Aa7_ELY4Ie5-xEd7e1uncAlx0Ug%3A1705173759335&ei=_-KiZZ-LFODd5OUPiP2iuA0&udm=&ved=0ahUKEwjfhtKhi9uDAxXgLrkGHYi-CNcQ4dUDCBA&uact=5&oq=euro+hoje&gs_lp=Egxnd3Mtd2l6LXNlcnAiCWV1cm8gaG9qZTIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzINEAAYgAQYigUYQxiwAzIZEC4YgAQYigUYQxjHARjRAxjIAxiwA9gBAjIZEC4YgAQYigUYQxjHARjRAxjIAxiwA9gBAkiDCFAAWKMHcAF4AZABAZgBgwKgAakJqgEFMC43LjG4AQPIAQD4AQHCAgoQIxiABBiKBRgnwgIQEAAYgAQYigUYQxixAxiDAcICChAAGIAEGIoFGEPCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGNEDwgIPECMYgAQYigUYJxhGGIICwgILEAAYgAQYsQMYgwHCAgUQABiABMICCxAuGIAEGLEDGIMBwgIZEAAYgAQYigUYRhiCAhiXBRiMBRjdBNgBAeIDBBgAIEGIBgGQBgu6BgYIARABGBO6BgQIAhgI&sclient=gws-wiz-serp")
    euro = page.locator('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text_content()
    euro = euro.replace(',', '.')
    print(f'The euro is coasting R${euro} brazilian real')

    convertion = input('Do you wish to make a convertion? [Y] Yes [N] No: ')

    if convertion == 'Y' or convertion == 'y':
        dol_eur = input('[1] Dolar [2] Euro: ')
        if dol_eur == '1':
            value = input('Input the value that you want to convert: ')
            result = float(dolar) * float(value)
            print(f'Result: R${result} brazilian real')
        elif dol_eur == '2':
            value = input('Input the value that you want to convert: ')
            result = float(euro) * float(value)
            print(f'Result: R${result} brazilian real')

    
    context.close()
    browser.close()
