
html_path = r"C:\repos\abekat\html\abe.html"

cnt: str
with open(html_path, mode="r") as file:
    cnt = file.read()

print(cnt)