# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MigrateDesktopsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        region_id: str = None,
        target_office_site_id: str = None,
    ):
        # The IDs of the cloud computers. You can specify 1 to 100 IDs.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the destination office network.
        # 
        # This parameter is required.
        self.target_office_site_id = target_office_site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_office_site_id is not None:
            result['TargetOfficeSiteId'] = self.target_office_site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetOfficeSiteId') is not None:
            self.target_office_site_id = m.get('TargetOfficeSiteId')

        return self

