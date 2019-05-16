from jinja2 import Markup


class momentjs(object):

    def __init__(self, timestamp):
        self.timestamp = timestamp

    # Wrapper to call moment.js method
    def render(self, format):
        return Markup(f"<script>\ndocument.write(moment(\"{self.timestamp}\").{format});\n</script>")
        # document.write(moment("{{ ann.date_pub }}").format("DD MMMM HH:mm"))

    # Format time
    def format(self, fmt="DD MMMM HH:mm"):
        return self.render(f"format(\"{fmt}\")")

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")