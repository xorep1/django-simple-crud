SETTING_MODULE="dev"

if SETTING_MODULE == "prod":
    from .prod import *
elif SETTING_MODULE == "dev":
    from .dev import *
    
else:
    from .dev import *