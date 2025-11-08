import requests

cn_url = "https://schaledb.com/data/cn/students.min.json"
jp_url = "https://schaledb.com/data/jp/students.min.json"

cn_data = requests.get(cn_url).json()
jp_data = requests.get(jp_url).json()

old_like='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
new_like='1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,3,3,8,8'

keys = cn_data.keys()
replace_dict = {}
for stu_id in keys:
    cn_name = cn_data[stu_id]["Name"]
    jp_name = jp_data[stu_id]["Name"].replace("（", " (").replace("）", ")").replace("バニーガール", "バニー")
    print(f"{stu_id}: {jp_name} -> {cn_name}")
    cn_data[stu_id]["name"] = jp_name
    replace_dict[jp_name] = cn_name

def replace_file(file_name):
    replaced_lines = []
    for line in open(file_name, "r", encoding="utf-8"):
        jp_name = line.split(",")[0]
        if old_like in line:
            line = line.replace(old_like, new_like)
            print(f"Replaced like values for: {jp_name}")
        if jp_name in replace_dict:
            cn_name = replace_dict[jp_name]
            line = line.replace(jp_name, cn_name)
            replaced_lines.append(line)
        else:
            if jp_name not in replace_dict.values():
                print(f"Not found: {line}")
            replaced_lines.append(line)
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(''.join(replaced_lines))

replace_file("../blue_archive_gift.csv")
replace_file("../blue_archive_student_img_path.csv")