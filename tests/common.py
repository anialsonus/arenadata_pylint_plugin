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

"""Common utils for testing checkers"""

import astroid

from pylint.testutils import Message, CheckerTestCase


class GeneralCheckerTest(CheckerTestCase):
    """
    Provide general functions to check positive and negative cases.
    You HAVE TO set NEGATIVE_CODE to negative message id
    """

    NEGATIVE_CODE: str

    def negative_case(self, code: str):
        """Check if assertion message is added on problem code"""
        node = astroid.extract_node(code)
        with self.assertAddsMessages(Message(msg_id=self.NEGATIVE_CODE, node=node)):
            self.checker.visit_assert(node)

    def positive_case(self, code: str):
        """Check if assertion message isn't added on code without problem"""
        node = astroid.extract_node(code)
        with self.assertNoMessages():
            self.checker.visit_assert(node)
