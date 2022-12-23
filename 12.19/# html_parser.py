import re


class HTMLParser:
    """
    Строитель для пошаговой обработки HTML документа.
    """
    single: set[str] = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, html_doc: str):
        self.html = html_doc

    def add_eol(self, before_value: bool = True):
        pattern = re.compile(r'<(!-- )?/?\w+.*?( --)?>', re.S)
        bf = '\n' if before_value else ''
        return HTMLParser(pattern.sub(rf'\n\g<0>{bf}', self.html))

    def optimize_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'\n{2,10}')
        return HTMLParser(pattern.sub('\n', self.html))

    def delete_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'>\s*<')
        return HTMLParser(pattern.sub('><', self.html))

    def delete_empty(self) -> 'HTMLParser':
        pattern = re.compile(r'<(?P<tag>\w+?)>\s*</(?P=tag)>', re.S)
        return HTMLParser(pattern.sub('', self.html))

    def delete_tags(self, *tags: str) -> 'HTMLParser':
        """Важно: теги контейнеры удаляются вместе со всем содержимым, включая любые вложенные теги!"""
        q = self.html
        for tag in set(tags) - self.single:
            pat_op = re.compile(rf'<{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            pat_cl = re.compile(rf'</{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            lt = len(tag)
            while mo := pat_op.search(q):
                if mo:
                    sl = 1 if mo['slash'] else 0
                    start, i = mo.start(), mo.end() - (lt + sl + 1)
                    c = 1
                    while True:
                        if mo := pat_op.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            i = mo.end() - (lt + sl + 1)
                            c += 1
                        elif mo := pat_cl.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            if c > 1:
                                i = mo.end() - (lt + sl + 1)
                            elif c == 1:
                                i += lt + 3
                            c -= 1
                        else:
                            i += lt + 3
                            c -= 1
                        if not c:
                            break
                    q = q[:start] + q[i:]

        for tag in set(tags) & self.single:
            pattern = re.compile(rf'<{tag}.*?>', re.S)
            q = pattern.sub('', q)

        return HTMLParser(q)

    def delete_attrs(self, *attrs: str, all: bool = False) -> 'HTMLParser':
        q = self.html
        if all:
            pattern = re.compile(r'<\w+?( .*?)?>', re.S)
            q = pattern.sub(r'<\g<name>>', q)
        else:
            for attr_key in attrs:
                pattern = re.compile(rf'\s+?{attr_key}=\".*?\"')
                q = pattern.sub('', q)
        return HTMLParser(q)

