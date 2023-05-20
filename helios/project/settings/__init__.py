import os

DEV_STAGES = "dev"
PROD_STAGES = "prod"

try:
    host_stage = os.environ.get('ENVIRONMENT')
    if host_stage in PROD_STAGES:
        from .prod import *
    elif host_stage in DEV_STAGES:
        from .dev import *
    else:
        raise Exception("invalid host")
except Exception:
    from .local import *