# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHybridMonitorSLSGroupRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        slsgroup_name: str = None,
    ):
        self.region_id = region_id
        # The name of the Logstore group.
        # 
        # For information about how to obtain the name of a Logstore group, see [DescribeHybridMonitorSLSGroup](https://help.aliyun.com/document_detail/429526.html).
        # 
        # This parameter is required.
        self.slsgroup_name = slsgroup_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slsgroup_name is not None:
            result['SLSGroupName'] = self.slsgroup_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SLSGroupName') is not None:
            self.slsgroup_name = m.get('SLSGroupName')

        return self

