import re
from pathlib import Path

app_path = Path('module4/broken_app/app.py')
content = app_path.read_text()

# Fix the case-sensitive variable reference: app_version -> APP_VERSION
fixed_content = re.sub(
    r'(version\s*=\s*)app_version(\s*#.*)?',
    r'\1APP_VERSION\2',
    content
)

app_path.write_text(fixed_content)
print('Fixed: Changed app_version to APP_VERSION in get_version function')