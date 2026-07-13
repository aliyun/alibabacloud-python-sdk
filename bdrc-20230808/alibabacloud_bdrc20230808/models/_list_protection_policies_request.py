# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProtectionPoliciesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        protection_policy_id: str = None,
        protection_policy_region_id: str = None,
    ):
        # The maximum number of results to return.
        self.max_results = max_results
        # The paging token.
        self.next_token = next_token
        # The protection policy ID.
        self.protection_policy_id = protection_policy_id
        # The region ID of the protection policy.
        self.protection_policy_region_id = protection_policy_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.protection_policy_id is not None:
            result['ProtectionPolicyId'] = self.protection_policy_id

        if self.protection_policy_region_id is not None:
            result['ProtectionPolicyRegionId'] = self.protection_policy_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProtectionPolicyId') is not None:
            self.protection_policy_id = m.get('ProtectionPolicyId')

        if m.get('ProtectionPolicyRegionId') is not None:
            self.protection_policy_region_id = m.get('ProtectionPolicyRegionId')

        return self

