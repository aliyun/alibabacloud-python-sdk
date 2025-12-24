# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRAMDirectoryRequest(DaraModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        directory_name: str = None,
        enable_admin_access: bool = None,
        enable_internet_access: bool = None,
        region_id: str = None,
        v_switch_id: List[str] = None,
    ):
        # The method in which the cloud computer is connected.
        # 
        # Valid values:
        # 
        # *   VPC
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Internet (default)
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Any
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.desktop_access_type = desktop_access_type
        # The directory name. The name must be 2 to 255 characters in length. It must start with a letter but cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.directory_name = directory_name
        # Specifies whether to grant the local administrator permissions to users that are authorized to use cloud computers in the office network.
        # 
        # Valid values:
        # 
        # *   <!-- -->
        # 
        #     true
        # 
        #     <!-- -->
        # 
        #     (default)
        # 
        #     <!-- -->
        # 
        # *   <!-- -->
        # 
        #     false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_admin_access = enable_admin_access
        # Specifies whether to enable Internet access.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_internet_access = enable_internet_access
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The vSwitch IDs. You can configure only one vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

