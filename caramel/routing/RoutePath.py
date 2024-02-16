import re

class RoutePath:
    def __init__(self, path):
        self.raw_path = path
        self.segments = []
        self.regex_pattern = ""
        self.param_names = []
        self.parse_path()

    def parse_path(self):
        # Convert path to a regex pattern
        pattern = re.sub(r'{([^{}:]+):?([^{}]*)}', self._replace_param, self.raw_path)
        self.regex_pattern = re.compile(f"^{pattern}$")

    def _replace_param(self, match):
        # Extract param name and optional regex
        param_name, regex = match.groups()
        self.param_names.append(param_name)
        return f"(?P<{param_name}>{regex or '[^/]+'})"  # Default regex matches everything except '/'

    def match(self, path):
        match = self.regex_pattern.match(path)
        if match:
            return {param: match.group(param) for param in self.param_names}
        else:
            return None

    