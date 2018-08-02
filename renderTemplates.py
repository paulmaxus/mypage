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

# variables to pass to context
pages = ['intro','research','events']
projects = ['nlp','shiny']
events = [
          [2018,
            [
              ['09','NE, Den Haag','Project meeting'
              ],
              ['07','NE, University Medical Center Groningen', 
              'Summer school on neural speech processing',
              '<a target="_blank" href="docs/maps.pdf">poster</a>'
              ],
              ['04','UK, Leicester','Experimental Psychology Society meeting',
              '<a target="_blank" href="docs/eps.pdf">poster</a>'
              ],
              ['03','NE, Nijmegen','Project meeting',
              '<a target="_blank" href="docs/nijmegen.pdf">presentation</a>'
              ]
            ]
          ],
          [2017,
            [
              ['10','ES, Vitoria','Project meeting and Python training'],
              ['07','EL, Heraklion','<a href="#char">Software project</a>, entrepreneurship in hearing technology, summer school on speech synthesis'
              ],
              ['04','UK, Edinburgh','Workshop on cognitive effort'
              ]
            ]
          ]
         ]

context = {
    'pages' : pages,
    'projects' : projects,
    'thisPage' : '',
    'events' : events
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
