# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMountTargetsRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        file_system_id: str = None,
        mount_target_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the region.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The name of the mount target.
        self.mount_target_name = mount_target_name
        # The number of the page to return. Pages start from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries returned per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_target_name is not None:
            result['MountTargetName'] = self.mount_target_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetName') is not None:
            self.mount_target_name = m.get('MountTargetName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

