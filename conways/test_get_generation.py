from unittest import TestCase
# I've submitted a question and I'm waiting for an answer now, because I really don't
# understand what's wrong with my code. For me, the test is wrong, but I'm probably missing
# something on the description. Here is the link to such question:
#
# https://www.codewars.com/kata/52423db9add6f6fc39000354/discuss#5936dba15189589f40000002


class TestGetGeneration(TestCase):
    @staticmethod
    def htmlize(array):
        s = []
        for row in array:
            for cell in row:
                s.append('▓▓' if cell else '░░')
            s.append('<br/>')
        return ''.join(s)

    # def test_get_generation(self):
    #     start = [[1, 0, 0],
    #              [0, 1, 1],
    #              [1, 1, 0]]
    #     end = [[0, 1, 0],
    #            [0, 0, 1],
    #            [1, 1, 1]]
    #     from ConwaysGameOfLife import get_generation
    #     resp = get_generation(start, 1)
    #     self.assertEquals(resp, end, 'Got<br/>' + self.htmlize(resp) + '<br/>instead of<br/>' + self.htmlize(end))

    def test_get_generation(self):
        start = [[1, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
        end = [[1, 0, 1],
               [0, 1, 1],
               [0, 1, 0]]
        from ConwaysGameOfLife import get_generation
        resp = get_generation(start, 2)
        self.assertEquals(resp, end, 'Got<br/>' + self.htmlize(resp) + '<br/>instead of<br/>' + self.htmlize(end))

# [[0, 1, 0],
#  [0, 0, 1],
#  [1, 1, 1]]