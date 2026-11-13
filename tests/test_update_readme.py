import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('update_readme', ROOT / 'scripts/update_readme.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.repos = json.loads((ROOT / 'tests/repos.json').read_text())
        self.descriptions = json.loads((ROOT / 'scripts/projects.json').read_text())

    def test_featured_order_and_profile_exclusion(self):
        selected = module.select_repos(self.repos, 'Geist-dev')
        self.assertEqual([r['name'] for r in selected[:3]], ['File-Storage', 'close-discord', 'Alias'])
        self.assertNotIn('Geist-dev', [r['name'] for r in selected])
        self.assertEqual(len(selected), 7)

    def test_exclude_private_forks_archives_and_other_owners(self):
        base = self.repos[0]
        bad = []
        for field, value in [('private', True), ('visibility', 'private'), ('fork', True), ('archived', True), ('owner', {'login': 'someone-else'})]:
            repo = copy.deepcopy(base)
            repo[field] = value
            bad.append(repo)
        self.assertEqual(module.select_repos(bad, 'Geist-dev'), [])

    def test_language_specific_descriptions_and_correct_alias_scope(self):
        selected = module.select_repos(self.repos, 'Geist-dev')
        en = module.format_table(selected, 'en', self.descriptions, 'Geist-dev')
        ru = module.format_table(selected, 'ru', self.descriptions, 'Geist-dev')
        self.assertIn('Browser word game', en)
        self.assertIn('Браузерная игра', ru)
        self.assertNotIn('Discord Activity', en)
        self.assertIn('Node.js · Express · WebSocket', en)

    def test_api_text_cannot_break_table_or_insert_html(self):
        repo = {'name': 'new-project', 'description': '<img src=x> | row\nnext', 'language': 'Python'}
        table = module.format_table([repo], 'en', {}, 'Geist-dev')
        self.assertNotIn('<img', table)
        self.assertIn('&lt;img src=x&gt; &#124; row next', table)
        self.assertEqual(len(table.splitlines()), 3)

    def test_replacement_preserves_handwritten_content_and_is_idempotent(self):
        before = 'Intro with \\1\n' + module.START + '\nold\n' + module.END + '\nContact'
        after = module.replace_section(before, 'new \\1')
        self.assertTrue(after.startswith('Intro with \\1\n'))
        self.assertTrue(after.endswith('\nContact'))
        self.assertIn('new \\1', after)
        self.assertEqual(module.replace_section(after, 'new \\1'), after)

    def test_bad_marker_pairs_are_rejected(self):
        for text in ['', module.START, module.END + module.START, module.START * 2 + module.END]:
            with self.assertRaises(ValueError):
                module.replace_section(text, 'replacement')

    def test_both_languages_are_validated_before_any_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'scripts').mkdir()
            (root / 'scripts/projects.json').write_text(json.dumps(self.descriptions))
            en = root / 'README.md'
            en.write_text(module.START + module.END)
            (root / 'README.ru.md').write_text('missing markers')
            before = en.read_text()
            with self.assertRaises(ValueError):
                module.update_documents(root, self.repos, 'Geist-dev')
            self.assertEqual(en.read_text(), before)

    def test_empty_catalog_does_not_erase_existing_content(self):
        with self.assertRaises(ValueError):
            module.update_documents(ROOT, [], 'Geist-dev')

    def test_readme_links_assets_contacts_and_markers(self):
        for filename, sibling in [('README.md', 'README.ru.md'), ('README.ru.md', 'README.md')]:
            text = (ROOT / filename).read_text()
            self.assertIn(f'href="{sibling}"', text)
            self.assertIn('https://t.me/flipgood', text)
            self.assertIn('mailto:aeromax.live@mail.ru', text)
            self.assertIn('Codex', text)
            self.assertIn('Claude', text)
            self.assertEqual(text.count(module.START), 1)
            self.assertEqual(text.count(module.END), 1)
            self.assertNotIn('herokuapp.com', text)
            for theme in ['dark', 'light']:
                self.assertTrue((ROOT / f'assets/header-{theme}.svg').is_file())


if __name__ == '__main__':
    unittest.main()
