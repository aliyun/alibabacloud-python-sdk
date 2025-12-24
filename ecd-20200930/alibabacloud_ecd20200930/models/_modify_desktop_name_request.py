# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDesktopNameRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        new_desktop_name: str = None,
        region_id: str = None,
    ):
        # The ID of the cloud computer.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The new name of the cloud computer. The name of the cloud computer must meet the following requirements:
        # 
        # *   The name must be 1 to 64 characters in length.
        # *   The name must start with a letter but cannot start with `http://` or `https://`.
        # *   The name can only contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.new_desktop_name = new_desktop_name
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
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
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.new_desktop_name is not None:
            result['NewDesktopName'] = self.new_desktop_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('NewDesktopName') is not None:
            self.new_desktop_name = m.get('NewDesktopName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

