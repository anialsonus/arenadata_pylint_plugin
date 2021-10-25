# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests on assertion message presence checker"""

from tests.common import GeneralCheckerTest
from src.ad_pylint_plugin.assertion_message import AssertMessageChecker


class TestAssertMessageChecker(GeneralCheckerTest):
    """Check positive and negative scenarios for AssertMessageChecker"""

    CHECKER_CLASS = AssertMessageChecker
    NEGATIVE_CODE = AssertMessageChecker.NO_MESSAGE

    def test_finds_no_message(self):
        """Message is not presented"""
        self.negative_case(
            """
            def fun_wo_assert_message():
                assert 1 == 2 #@
            """
        )

    def test_finds_empty_message(self):
        """Message is empty"""
        self.negative_case(
            """
            def fun_empty_assert_message():
                assert 1 == 2, '' #@
            """
        )

    def test_finds_fine_message(self):
        """Message is provided as string"""
        self.positive_case(
            """
            def func_with_assert_message():
                assert 1 == 2, "Assert message that makes sense" #@
            """
        )

    def test_f_string(self):
        """Message is provided as formatted string"""
        self.positive_case(
            """
            def func():
                some = 12
                assert 1 == 2, f"Some {some}" #@
            """
        )

    def test_callable(self):
        """Message is provided as callable"""
        self.positive_case(
            """
            def get_me_there():
                return "Something else"

            def func():
                assert 1 == 2, get_me_there() #@
            """
        )
