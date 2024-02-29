# apply_creds_linux.py: update various creds (linux version)
import os
import json
import yaml

# read creds
fn = "~/rlf/test_data.yaml"
with open(fn, "rt", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# write permanent env vars
cmd_text = "written by apply_creds_linux.py\n\n"
for name in ["wandb_api_key", "tpx_sql_pw", "openai_api_key"]:
    value = data[name]["value"]
    cmd = f"export {name.upper()}={value}"
    cmd_text += cmd + "\n"

# append this to .bashrc
fn = "~/.bashrc"
with open(fn, "a") as f:
    f.write(cmd_text)

# write azure store files
for store in data["azure_stores"]:
    fn = "~/.xt/stores/{}/keys.bin".format(store)
    # create dir, if needed
    os.makedirs(os.path.dirname(fn), exist_ok=True)

    with open(fn, "wt") as f:
        store_dict = data["azure_stores"][store]
        jtext = json.dumps(store_dict, indent=4)
        f.write(jtext)

# write .git-credentials
fn = "~/.git-credentials"
gc = data["git_credentials"]["value"]
with open(fn, "wt") as f:
    f.write(gc)
    
