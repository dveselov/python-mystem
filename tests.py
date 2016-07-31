import unittest
import mystem

class SimpleRegressionTestCase(unittest.TestCase):

    def test_get_lemma(self):
        with mystem.analyze("санкт-петербурге") as lemms:
            lemma = lemms[0]
            self.assertEqual(str(lemma), "санкт-петербург")
            self.assertEqual(lemma.form, "санкт-петербурге")
            self.assertIn(mystem.Grammeme.Geo, lemma.stem_grammemes)
            self.assertIn(mystem.Grammeme.Singular, sum(lemma.flex_grammemes, []))
