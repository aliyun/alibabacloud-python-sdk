# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAbacPolicyRequest(DaraModel):
    def __init__(
        self,
        abac_policy_id: int = None,
        tid: int = None,
    ):
        # The ID of the policy.
        # 
        # This parameter is required.
        self.abac_policy_id = abac_policy_id
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abac_policy_id is not None:
            result['AbacPolicyId'] = self.abac_policy_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbacPolicyId') is not None:
            self.abac_policy_id = m.get('AbacPolicyId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

