# NOTE

class Note(object):
    # 시작
    def __init__(self, content = None):
        self.content = content
    # 쓰기
    def write_content(self, content):
        self.content = content
    # 삭제
    def remove_all(self):
        self.content = ""
    # 추가
    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content