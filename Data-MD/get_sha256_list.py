
def get_sha256(load_txt):
    sha256_list = []
    with open(load_txt, 'r') as f:
        data_list = eval(f.read())

        for item in data_list:
            sha256 = item[0].split("\\")[2]
            sha256_list.append(sha256)
    return sha256_list

print(get_sha256("train.txt"))
print(get_sha256("test.txt"))
