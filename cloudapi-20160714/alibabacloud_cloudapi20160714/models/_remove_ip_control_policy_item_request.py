# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveIpControlPolicyItemRequest(DaraModel):
    def __init__(
        self,
        ip_control_id: str = None,
        policy_item_ids: str = None,
        security_token: str = None,
    ):
        # The ID of the ACL. The ID is unique.
        # 
        # This parameter is required.
        self.ip_control_id = ip_control_id
        # The ID of a policy. Separate multiple IDs with semicolons (;). A maximum of 100 IDs can be entered.
        # 
        # This parameter is required.
        self.policy_item_ids = policy_item_ids
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id

        if self.policy_item_ids is not None:
            result['PolicyItemIds'] = self.policy_item_ids

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('PolicyItemIds') is not None:
            self.policy_item_ids = m.get('PolicyItemIds')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

