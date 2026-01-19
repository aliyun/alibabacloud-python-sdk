# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpControlPolicyItemsRequest(DaraModel):
    def __init__(
        self,
        ip_control_id: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_item_id: str = None,
        security_token: str = None,
    ):
        # The ID of the ACL. The ID is unique.
        self.ip_control_id = ip_control_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The ID of the policy.
        self.policy_item_id = policy_item_id
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

