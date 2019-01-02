from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        # print (results[-2] + '.' + results[-1])
        return results[-2] + '.' + results[-1]
    except:
        return ''
        # print('error in domain')


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        # print ("help : " + urlparse(url).netloc)
        return urlparse(url).netloc
    except:
        return ''
        # print ('error in subdomain')

# get_domain_name('https://www.knit.ac.in')
# get_sub_domain_name('https://www.knit.ac.in')