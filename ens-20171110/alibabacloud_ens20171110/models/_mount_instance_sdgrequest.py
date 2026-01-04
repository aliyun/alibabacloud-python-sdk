# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MountInstanceSDGRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        sdgid: str = None,
    ):
        # The IDs of the instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The ID of the SDG.
        # 
        # This parameter is required.
        self.sdgid = sdgid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

