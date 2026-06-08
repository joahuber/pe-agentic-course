import re
from pathlib import Path

app_path = Path('module4/broken_app/app.py')
content = app_path.read_text()

# Fix the NameError: change 'app_version' to 'APP_VERSION' in get_version function
fixed_content = re.sub(
    r'version = app_version(\s+# Bug 2:.*)?',
    'version = APP_VERSION',
    content
)

app_path.write_text(fixed_content)
print('Fixed: Changed app_version to APP_VERSION in get_version() function')