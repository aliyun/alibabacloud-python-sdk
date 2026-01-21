# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddInstanceRdMemberRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        member_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.member_id = member_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

