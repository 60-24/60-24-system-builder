import json
import tempfile
import unittest
from pathlib import Path

from src.system_builder.core import build_plan, generate, load_intent


class BuilderCoreTests(unittest.TestCase):
    def make_intent(self, files=None):
        return {"version": 1, "files": files or [{"path": "a.txt", "content": "A"}]}

    def test_load_valid_intent(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "intent.json"
            path.write_text(json.dumps(self.make_intent()), encoding="utf-8")
            self.assertEqual(load_intent(path)["version"], 1)

    def test_reject_wrong_version(self):
        with self.assertRaises(ValueError):
            build_plan({"version": 2, "files": [{"path": "a", "content": "x"}]})

    def test_reject_absolute_path(self):
        with self.assertRaises(ValueError):
            build_plan(self.make_intent([{"path": "/tmp/a", "content": "x"}]))

    def test_reject_parent_traversal(self):
        with self.assertRaises(ValueError):
            build_plan(self.make_intent([{"path": "../escape", "content": "x"}]))

    def test_plan_is_sorted(self):
        plan = build_plan(self.make_intent([
            {"path": "z.txt", "content": "z"}, {"path": "a.txt", "content": "a"}]))
        self.assertEqual([item["path"] for item in plan], ["a.txt", "z.txt"])

    def test_generate_manifest_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = generate(self.make_intent(), Path(tmp) / "out")
            self.assertEqual(len(manifest["files"][0]["sha256"]), 64)
            self.assertTrue((Path(tmp) / "out" / "manifest.json").exists())

    def test_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "out"
            generate(self.make_intent(), out)
            with self.assertRaises(FileExistsError):
                generate(self.make_intent(), out)


if __name__ == "__main__":
    unittest.main()
