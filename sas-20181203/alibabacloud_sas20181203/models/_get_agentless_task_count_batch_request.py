# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAgentlessTaskCountBatchRequest(DaraModel):
    def __init__(
        self,
        target_type: int = None,
        uuid_list: List[str] = None,
    ):
        # The detection object type. Valid values:
        # 
        # - **1**: host snapshot
        # - **2**: host image
        # - **3**: user snapshot
        # - **4**: user image
        # - **5**: NAS file system
        # - **6**: parallel sandbox
        # - **7**: security fix
        self.target_type = target_type
        # The list of resource UUIDs to query. The list can contain 1 to 100 elements.
        # 
        # This parameter is required.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

