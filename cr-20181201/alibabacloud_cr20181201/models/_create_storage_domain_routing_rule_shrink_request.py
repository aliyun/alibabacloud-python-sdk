# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStorageDomainRoutingRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        routes_shrink: str = None,
    ):
        # The instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The route list
        # 
        # This parameter is required.
        self.routes_shrink = routes_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.routes_shrink is not None:
            result['Routes'] = self.routes_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Routes') is not None:
            self.routes_shrink = m.get('Routes')

        return self

