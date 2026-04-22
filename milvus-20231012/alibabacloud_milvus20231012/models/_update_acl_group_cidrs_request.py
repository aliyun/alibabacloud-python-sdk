# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAclGroupCidrsRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        new_cidrs: str = None,
    ):
        self.group_name = group_name
        self.instance_id = instance_id
        self.new_cidrs = new_cidrs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.new_cidrs is not None:
            result['newCidrs'] = self.new_cidrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('newCidrs') is not None:
            self.new_cidrs = m.get('newCidrs')

        return self

