import requests


res_pars_list = []

resp = requests.get("https://coinmarketcap.com/")
resp_text = resp.text
parse = resp_text.split("<span>")
for parse_elem1 in parse:
    if parse_elem1.startswith("$"):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2.startswith("$") and parse_elem2[1].isdigit() :
                res_pars_list.append(parse_elem2)



bitcoin = res_pars_list[0]
dogecoin = res_pars_list[7]

print("Bitcoin: ", bitcoin," /|||\ Dogecoin: ", dogecoin)