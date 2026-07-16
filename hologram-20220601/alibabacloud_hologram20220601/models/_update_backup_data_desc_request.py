# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBackupDataDescRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        desc: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.desc = desc
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.desc is not None:
            result['desc'] = self.desc

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

