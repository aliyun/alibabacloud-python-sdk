# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDesktopHostNameRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_ids: List[str] = None,
        new_host_name: str = None,
        region_id: str = None,
    ):
        # The ID of the cloud desktop.
        self.desktop_id = desktop_id
        self.desktop_ids = desktop_ids
        # The new hostname of the cloud desktop. The hostname must meet the following requirements:
        # 
        # - The hostname must be 2 to 15 characters in length.
        # 
        # - The hostname can contain letters, digits, and hyphens (-). It cannot start or end with a hyphen, contain consecutive hyphens, or consist of only digits.
        # 
        # This parameter is required.
        self.new_host_name = new_host_name
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the available regions for Elastic Desktop Service.
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

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.new_host_name is not None:
            result['NewHostName'] = self.new_host_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('NewHostName') is not None:
            self.new_host_name = m.get('NewHostName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

