# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAbacPolicyRequest(DaraModel):
    def __init__(
        self,
        abac_policy_content: str = None,
        abac_policy_desc: str = None,
        abac_policy_id: int = None,
        abac_policy_name: str = None,
        tid: int = None,
    ):
        # The content of the policy.
        self.abac_policy_content = abac_policy_content
        # The description of the policy.
        self.abac_policy_desc = abac_policy_desc
        # The ID of the policy.
        # 
        # This parameter is required.
        self.abac_policy_id = abac_policy_id
        # The name of the permission policy.
        self.abac_policy_name = abac_policy_name
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the DMS console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abac_policy_content is not None:
            result['AbacPolicyContent'] = self.abac_policy_content

        if self.abac_policy_desc is not None:
            result['AbacPolicyDesc'] = self.abac_policy_desc

        if self.abac_policy_id is not None:
            result['AbacPolicyId'] = self.abac_policy_id

        if self.abac_policy_name is not None:
            result['AbacPolicyName'] = self.abac_policy_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbacPolicyContent') is not None:
            self.abac_policy_content = m.get('AbacPolicyContent')

        if m.get('AbacPolicyDesc') is not None:
            self.abac_policy_desc = m.get('AbacPolicyDesc')

        if m.get('AbacPolicyId') is not None:
            self.abac_policy_id = m.get('AbacPolicyId')

        if m.get('AbacPolicyName') is not None:
            self.abac_policy_name = m.get('AbacPolicyName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

