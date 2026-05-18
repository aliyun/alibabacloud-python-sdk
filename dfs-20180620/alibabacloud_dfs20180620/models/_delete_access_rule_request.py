# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccessRuleRequest(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        input_region_id: str = None,
    ):
        # This parameter is required.
        self.access_group_id = access_group_id
        # This parameter is required.
        self.access_rule_id = access_rule_id
        # This parameter is required.
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        return self

