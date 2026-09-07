# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDesktopNameRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_ids: List[str] = None,
        new_desktop_name: str = None,
        region_id: str = None,
        user_assign_mode: str = None,
    ):
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The list of cloud computer IDs.
        self.desktop_ids = desktop_ids
        # The new name of the cloud computer. The name must meet the following requirements:
        # 
        # - The name cannot exceed 64 characters in length.
        # - The name must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        # - The name can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), or hyphens (-).
        self.new_desktop_name = new_desktop_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user assignment mode.
        self.user_assign_mode = user_assign_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.new_desktop_name is not None:
            result['NewDesktopName'] = self.new_desktop_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('NewDesktopName') is not None:
            self.new_desktop_name = m.get('NewDesktopName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')

        return self

