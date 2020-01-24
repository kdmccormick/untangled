"""
Test Untangled.
"""
from pathlib import Path
from unittest import TestCase

import untangled

TEST_DATA_DIR_NAME = "test-data"


class UntangledTestCase(TestCase):
    """
    Test Untangled.
    """

    # pylint: disable=no-self-use

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.verify_test_data()

    @classmethod
    def verify_test_data(cls):
        """
        Fail if test materials aren't provisioned.
        """
        untangled_root = Path(untangled.__file__).resolve().parent
        test_materials_root = untangled_root.parent / TEST_DATA_DIR_NAME
        registrar_apps = test_materials_root / "registrar" / "registrar" / "apps"
        assert registrar_apps.exists(), (
            "Could not find test project; "
            "maybe you need to run 'make provision-tests'?"
        )

    def test_placeholder(self):
        """
        Test placeholder run function.
        """
        assert untangled.run() == 42
