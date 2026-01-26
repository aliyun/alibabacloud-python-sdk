# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDispatchRuleRequest(DaraModel):
    def __init__(
        self,
        dispatch_rule: str = None,
        region_id: str = None,
    ):
        # The dispatch rule configuration. The value is a JSON string. For more information about this parameter, see the following **additional information about the DispatchRule parameter**.
        # 
        # This parameter is required.
        self.dispatch_rule = dispatch_rule
        # The ID of the region.
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
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

