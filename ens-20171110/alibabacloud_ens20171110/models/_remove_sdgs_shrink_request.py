# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveSDGsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        sdg_ids_shrink: str = None,
    ):
        # The IDs of the instances.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The IDs of SDG.
        self.sdg_ids_shrink = sdg_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.sdg_ids_shrink is not None:
            result['SdgIds'] = self.sdg_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('SdgIds') is not None:
            self.sdg_ids_shrink = m.get('SdgIds')

        return self

