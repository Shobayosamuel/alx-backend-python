#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google', {'value': 'google'}),
        ('abc', {'value': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_result: Dict,
                 mock_function: MagicMock) -> None:
        mock_function.return_value = MagicMock(return_value=expected_result)
        gh_client = GithubOrgclient(org_name)
        self.assertEqual(gh_client.org(), expected_response)
        mock_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
