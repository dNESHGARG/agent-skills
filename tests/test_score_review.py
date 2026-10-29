import unittest
from scripts.score_review import score

CASE = {"id": "example", "expected": [{"id": "issue", "severity": "P1"}]}

class ScoringTests(unittest.TestCase):
    def test_complete_finding(self):
        review = {"findings": [{"id":"issue","severity":"P1","trigger":"t","invariant":"i","fix":"f","test":"x"}]}
        self.assertEqual(score(CASE,review)["score"],5)

    def test_missing_finding(self):
        result = score(CASE,{"findings":[]})
        self.assertEqual(result["score"],0)
        self.assertEqual(result["missed"],["issue"])

    def test_unsupported_critical_claim_penalty(self):
        review = {"findings":[{"id":"unmatched","severity":"P1"}]}
        self.assertEqual(score(CASE,review)["score"],-1)

    def test_duplicate_id_cannot_score_twice(self):
        finding = {"id":"issue","severity":"P1","trigger":"t","invariant":"i","fix":"f","test":"x"}
        self.assertEqual(score(CASE,{"findings":[finding,finding]})["score"],4)

if __name__ == "__main__":
    unittest.main()
