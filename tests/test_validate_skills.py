import tempfile
import unittest
from pathlib import Path
from scripts.validate_skills import validate


class ValidatorTests(unittest.TestCase):
    def test_valid_skill(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'review' / 'SKILL.md'
            path.parent.mkdir()
            path.write_text('---\nname: review\ndescription: A long and useful description of this workflow\n---\n# Review\n' + 'Detailed steps. ' * 45)
            self.assertEqual(validate(path), [])

    def test_rejects_mismatched_name(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'review' / 'SKILL.md'
            path.parent.mkdir()
            path.write_text('---\nname: wrong\ndescription: A long and useful description of this workflow\n---\n# Review\n' + 'Detailed steps. ' * 45)
            self.assertTrue(any('directory' in error for error in validate(path)))

    def test_rejects_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'review' / 'SKILL.md'
            path.parent.mkdir()
            path.write_text('# No metadata\n')
            self.assertTrue(validate(path))


if __name__ == '__main__':
    unittest.main()
