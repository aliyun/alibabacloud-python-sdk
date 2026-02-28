# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVccGrantRuleRequest(DaraModel):
    def __init__(
        self,
        er_id: str = None,
        grant_rule_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        self.er_id = er_id
        # Authorization Entry ID
        # 
        # This parameter is required.
        self.grant_rule_id = grant_rule_id
        # Network Instance ID
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

