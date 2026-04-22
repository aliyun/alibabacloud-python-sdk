# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAclGroupRequest(DaraModel):
    def __init__(
        self,
        cidrs: str = None,
        group_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.cidrs = cidrs
        self.group_name = group_name
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidrs is not None:
            result['cidrs'] = self.cidrs

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidrs') is not None:
            self.cidrs = m.get('cidrs')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

