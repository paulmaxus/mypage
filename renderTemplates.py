# when running from within RStudio, you have to add anaconda to the path first
# 
# Sys.setenv(PATH = paste("/Users/massimo/anaconda/bin", Sys.getenv("PATH"),sep=":"))
# system("python --version")

import os
from jinja2 import Environment, FileSystemLoader

path = os.path.dirname('/Users/massimo/webpage/mypage/')
env = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(path, 'templates')),
    trim_blocks=False
)

# function for rendering templates in the environment
def render_template(filename, context):
    return env.get_template(filename).render(context)

pages = ['home','research','statistics','blog']
context = {
    'pages' : pages,
    'thisPage' : ''
}

outPath = 'mypage/website/'
f2render = ['home','research','statistics','blog']

for file in f2render:
    outFile = outPath + file + '.html'
    with open(outFile, 'w') as f:
        context['thisPage'] = file
        page = render_template(file+'.html', context)
        f.write(page)
