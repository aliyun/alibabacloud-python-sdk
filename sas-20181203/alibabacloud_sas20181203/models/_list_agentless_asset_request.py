# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentlessAssetRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        disk_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        page_size: int = None,
        platform: str = None,
        scan_region_id: str = None,
        target_type: int = None,
    ):
        # The page number in a paginated query.
        self.current_page = current_page
        # The type of the cloud disk. Values:
        # 
        # - **system**: System disk
        # 
        # - **data**: Data disk
        self.disk_type = disk_type
        # The ID of the asset instance.
        self.instance_id = instance_id
        # The name of the asset instance.
        self.instance_name = instance_name
        # The maximum number of items to return per page in a paginated query.
        self.page_size = page_size
        # The type of the operating system.
        self.platform = platform
        # The region ID.
        self.scan_region_id = scan_region_id
        # The type of the detection target. Values:
        # 
        # - **3**: User snapshot
        # 
        # - **4**: User-defined image
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.scan_region_id is not None:
            result['ScanRegionId'] = self.scan_region_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ScanRegionId') is not None:
            self.scan_region_id = m.get('ScanRegionId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

