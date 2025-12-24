# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DisableDesktopsInGroupRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_ids: List[str] = None,
        region_id: str = None,
    ):
        # The ID of the cloud computer share.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The IDs of the cloud computers.
        # 
        # This parameter is required.
        self.desktop_ids = desktop_ids
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

