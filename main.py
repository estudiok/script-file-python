from string import Template
import utils
import shutil
from jinja2 import Template


tm = Template("Hello {{ name }}")

msg = tm.render(name="Kola Song")

print(msg)

# names = None
# urls = None
# dates = None

# with open("names.txt") as f:
#     names = [x.strip() for x in f.readlines()]
# with open("urls.txt") as f:
#     urls = [x.strip() for x in f.readlines()]
# with open("dates.txt") as f:
#     dates = [x.strip() for x in f.readlines()]


# d = {
#     'title': 'This is the title'
# }

# with open('template.txt', 'r') as f:
#     src = Template(f.read())
#     result = src.substitute(d)
#     print(result)

# whith open('')


# temp_str = utils.templatePostData()
# temp_obj = Template(temp_str)
# temp_obj.substitute(
#                     image = "$image",
#                     autor = "$autor",
#                     link1 = "$link1",
#                     link2 = "link2",
#                     link3 = "link3"
#                    )
# print(temp_obj)

# shutil.copyfile('template-post/post-first.txt', 'perro.txt')



