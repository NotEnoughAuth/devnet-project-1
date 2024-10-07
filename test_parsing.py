import parse_data as parse
import unittest

class TestParse(unittest.TestCase):
    def test_parseYaml(self):
        self.assertEqual(parse.parseYaml('test.yaml'), {'name': 'John', 'age': 30, 'car': {'make': 'Toyota', 'model': 'Corolla', 'year': 2015}})
        
    def test_parseJson(self):
        self.assertEqual(parse.parseJson('test.json'), {'name': 'John', 'age': 30, 'car': {'make': 'Toyota', 'model': 'Corolla', 'year': 2015}})
        
    def test_parseXml(self):
        self.assertEqual(parse.parseXml('test.xml').tag, 'person')
        self.assertEqual(parse.parseXml('test.xml')[0].text, 'John')
        self.assertEqual(parse.parseXml('test.xml')[1].text, '30')
        self.assertEqual(parse.parseXml('test.xml')[2].tag, 'car')
        self.assertEqual(parse.parseXml('test.xml')[2][0].text, 'Toyota')
        self.assertEqual(parse.parseXml('test.xml')[2][1].text, 'Corolla')
        self.assertEqual(parse.parseXml('test.xml')[2][2].text, '2015')

if __name__ == '__main__':
    unittest.main()