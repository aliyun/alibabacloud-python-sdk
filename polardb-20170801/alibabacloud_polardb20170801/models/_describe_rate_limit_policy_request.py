# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRateLimitPolicyRequest(DaraModel):
    def __init__(
        self,
        gw_cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_id: str = None,
        region_id: str = None,
        scope_ref_id: str = None,
        scope_type: str = None,
    ):
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.policy_id = policy_id
        self.region_id = region_id
        self.scope_ref_id = scope_ref_id
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope_ref_id is not None:
            result['ScopeRefId'] = self.scope_ref_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScopeRefId') is not None:
            self.scope_ref_id = m.get('ScopeRefId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

