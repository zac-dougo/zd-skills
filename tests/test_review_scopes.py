"""Exercise the Git comparisons documented by code-review in isolated repos."""

from pathlib import Path
import subprocess
import tempfile
import unittest


class ReviewScopes(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.repo = Path(self.directory.name)
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Review fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'commit.gpgSign', 'false')

    def git(self, *args):
        return subprocess.check_output(
            ['git', *args], cwd=self.repo, text=True, stderr=subprocess.PIPE
        ).strip()

    def write(self, name, text):
        (self.repo / name).write_text(text)

    def commit(self, message):
        self.git('add', '--all')
        self.git('commit', '-m', message)
        return self.git('rev-parse', 'HEAD')

    def names(self, *args):
        return set(self.git(*args).splitlines())

    def test_staged_unstaged_and_untracked_are_distinct(self):
        self.write('staged.txt', 'original\n')
        self.write('unstaged.txt', 'original\n')
        self.commit('Initial fixture')
        self.write('staged.txt', 'staged correction\n')
        self.git('add', 'staged.txt')
        self.write('unstaged.txt', 'local correction\n')
        self.write('new.txt', 'new behaviour\n')

        self.assertEqual(self.names('diff', '--cached', '--name-only'), {'staged.txt'})
        self.assertEqual(self.names('diff', '--name-only'), {'unstaged.txt'})
        self.assertEqual(
            self.names('diff', 'HEAD', '--name-only'), {'staged.txt', 'unstaged.txt'}
        )
        self.assertEqual(
            self.names('ls-files', '--others', '--exclude-standard'), {'new.txt'}
        )

    def test_exact_revision_is_not_branch_merge_base(self):
        self.write('common.txt', 'original\n')
        self.commit('Common ancestor')
        self.git('switch', '-c', 'feature')
        self.write('feature.txt', 'feature\n')
        head = self.commit('Feature change')
        self.git('switch', 'main')
        self.write('base-only.txt', 'base change\n')
        base = self.commit('Base branch change')
        ancestor = self.git('merge-base', base, head)

        self.assertEqual(
            self.names('diff', base, head, '--name-only'),
            {'base-only.txt', 'feature.txt'},
        )
        self.assertEqual(
            self.names('diff', ancestor, head, '--name-only'), {'feature.txt'}
        )

    def test_branch_with_local_changes_preserves_all_requested_layers(self):
        self.write('original.txt', 'original\n')
        base = self.commit('Common ancestor')
        self.git('switch', '-c', 'feature')
        self.write('feature.txt', 'committed feature\n')
        self.commit('Feature change')
        self.write('original.txt', 'local change\n')
        self.write('new.txt', 'untracked change\n')
        ancestor = self.git('merge-base', base, 'HEAD')

        self.assertEqual(
            self.names('diff', ancestor, '--name-only'), {'original.txt', 'feature.txt'}
        )
        self.assertEqual(
            self.names('ls-files', '--others', '--exclude-standard'), {'new.txt'}
        )

    def test_unborn_branch_does_not_require_head(self):
        self.write('first.txt', 'staged\n')
        self.git('add', 'first.txt')
        self.write('first.txt', 'also unstaged\n')
        self.write('new.txt', 'untracked\n')
        self.assertEqual(self.names('diff', '--cached', '--name-only'), {'first.txt'})
        self.assertEqual(self.names('diff', '--name-only'), {'first.txt'})
        self.assertEqual(
            self.names('ls-files', '--others', '--exclude-standard'), {'new.txt'}
        )


if __name__ == '__main__':
    unittest.main()
