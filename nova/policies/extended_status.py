# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.policies import base


BASE_POLICY_NAME = 'os_compute_api:os-extended-status'


extended_status_policies = [
    base.create_rule_default(
        BASE_POLICY_NAME,
        base.RULE_ADMIN_OR_OWNER,
        """Return extended status in the response of server.

This policy will control the visibility for a set of attributes:
    OS-EXT-STS:task_state
    OS-EXT-STS:vm_state
    OS-EXT-STS:power_state
""",
        [
            {
                'method': 'GET',
                'path': '/servers/{id}'
            },
            {
                'method': 'GET',
                'path': '/servers/detail'
            }
        ]),
]


def list_rules():
    return extended_status_policies
