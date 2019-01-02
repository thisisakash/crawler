#Crawler#
###Overview###
This project will you grab all the links in a website by just providing the **name of the website** and the **name of the project**.
###Description###
The project can be best explained with the help of an example:
* Open **main.py** file
* Enter the **PROJECT_NAME**. Eg:  
PROJECT_NAME = 'wsvincent'
* Enter the **HOMEPAGE**. Eg:  
HOMEPAGE = 'https://wsvincent.com/'
* Run the **main.py** file.

**RESULT:** The crawler starts grabbing the link and puts uncrawled links in (for eg) _wsvincent/queue.txt_ and crawled links in (for eg) _wsvincent/crawled.txt_.

When it is done, there would be no links in the _queue.txt_ file.
