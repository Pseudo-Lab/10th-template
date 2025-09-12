import re, yaml, pathlib

tpl = pathlib.Path("README-template.md").read_text(encoding="utf-8")
cfg = yaml.safe_load(pathlib.Path("config.yml").read_text(encoding="utf-8"))

def replace_all(text, mapping):
    # {{키}} 형태만 찾아 치환
    for k, v in mapping.items():
        text = re.sub(r"{{\s*" + re.escape(str(k)) + r"\s*}}", str(v), text)
    return text

out = replace_all(tpl, cfg)
pathlib.Path("README.md").write_text(out, encoding="utf-8")
print("README.md 갱신 완료!")
