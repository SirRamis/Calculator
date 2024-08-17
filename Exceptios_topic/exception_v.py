def main():
    d = {'website': 'google'}
    try:
        print(asdf)
        data = d['url']
    except:
        data = 'https://'
        print('Inside except', data)
        return data
    finally:
        print('Very important action')

result = main()
print(result)