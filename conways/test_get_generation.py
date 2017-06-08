from unittest import TestCase
from ConwaysGameOfLife import get_generation


class TestGetGeneration(TestCase):
    def test_get_generation1(self):
        start = [[1, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
        end1 = [[0, 1, 0],
                [0, 0, 1],
                [1, 1, 1]]
        resp = get_generation(start, 1)
        self.assertEquals(resp, end1, 'Got<br/>' + str(resp) + '<br/>instead of<br/>' + str(end1))

    def test_get_generation2(self):
        start = [[1, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
        end2 = [[1, 0, 1],
                [0, 1, 1],
                [0, 1, 0]]
        resp = get_generation(start, 2)
        self.assertEquals(resp, end2, 'Got<br/>' + str(resp) + '<br/>instead of<br/>' + str(end2))

    def test_get_generation40(self):
        start = [[1, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
        end40 = [[1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1],
                 [1, 1, 1, 1, 0, 0]]
        resp = get_generation(start, 40)
        self.assertEquals(resp, end40, 'Got<br/>' + str(resp) + '<br/>instead of<br/>' + str(end40))
