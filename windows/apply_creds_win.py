# apply_creds_win.py: update various creds (windows version)
import os
import json
import yaml

# read creds
fn = "c:/rlf/test_data.yaml"
with open(fn, "rt", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# write permanent env vars
for name in ["wandb_api_key", "tpx_sql_pw", "openai_api_key", "anthropic_api_key", "groq_api_key", "google_api_key", "together_api_key", "hyperbolic_api_key"]:
    value = data[name]["value"]
    cmd = f"setx {name.upper()} {value}"
    os.system(cmd)

# write azure store files
for store in data["azure_stores"]:
    fn = "{}/.xt/stores/{}/keys.bin".format(os.getenv("USERPROFILE"), store)
    # create dir, if needed
    os.makedirs(os.path.dirname(fn), exist_ok=True)

    with open(fn, "wt") as f:
        store_dict = data["azure_stores"][store]
        jtext = json.dumps(store_dict, indent=4)
        f.write(jtext)

