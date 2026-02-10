# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupedTagsRequest(DaraModel):
    def __init__(
        self,
        machine_types: str = None,
    ):
        # The type of the asset to query. If you do not specify this parameter, the tags of all asset types are queried. Valid values:
        # 
        # *   **ecs**: server
        # *   **cloud_product**: Alibaba Cloud service
        self.machine_types = machine_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        return self

