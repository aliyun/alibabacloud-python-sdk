# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSDGsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        sdgids_shrink: str = None,
    ):
        # The AIC instance ID to be queried.
        self.instance_ids_shrink = instance_ids_shrink
        # The IDs of SDGs that you want to query. By default, all SDGs are queried.
        self.sdgids_shrink = sdgids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.sdgids_shrink is not None:
            result['SDGIds'] = self.sdgids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('SDGIds') is not None:
            self.sdgids_shrink = m.get('SDGIds')

        return self

