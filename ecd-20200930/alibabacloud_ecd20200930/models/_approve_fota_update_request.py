# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveFotaUpdateRequest(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        desktop_id: str = None,
        region_id: str = None,
    ):
        # Mirror version.
        # 
        # This parameter is required.
        self.app_version = app_version
        # The ID of the cloud computer.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by Elastic Desktop Service.
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
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

