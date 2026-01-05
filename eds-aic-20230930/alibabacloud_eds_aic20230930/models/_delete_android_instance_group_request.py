# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAndroidInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
    ):
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        return self

