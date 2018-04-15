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

pages = ['intro','research']
projects = ['shiny','nlp']
context = {
    'pages' : pages,
    'projects' : projects,
    'thisPage' : ''
}

outPath = 'mypage/website/'
#f2render = ['index','research','projects','blog']
f2render = ['index']

for file in f2render:
    outFile = outPath + file + '.html'
    with open(outFile, 'w') as f:
        context['thisPage'] = file
        page = render_template(file+'.html', context)
        f.write(page)
