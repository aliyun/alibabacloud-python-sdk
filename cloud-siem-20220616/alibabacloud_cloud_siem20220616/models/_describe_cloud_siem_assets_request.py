# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudSiemAssetsRequest(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        asset_type: str = None,
        asset_uuid: str = None,
        current_page: int = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The asset name.
        self.asset_name = asset_name
        # The asset type. Valid values:
        # 
        # - ip: IP address
        # 
        # - domain: domain name
        # 
        # - url: URL
        # 
        # - process: process
        # 
        # - file: file
        # 
        # - host: host
        self.asset_type = asset_type
        # The UUID of the asset.
        self.asset_uuid = asset_uuid
        # The page number. The value must be greater than or equal to 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # The number of entries to return on each page. The maximum value is 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the Data Management center of Threat Analysis is deployed. Select a region based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: assets in the Chinese mainland or China (Hong Kong)
        # 
        # - ap-southeast-1: assets outside China
        self.region_id = region_id
        # The user ID of the member whose data you want to view. This parameter is available only when an administrator wants to switch to the perspective of a member.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts that belong to the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.asset_uuid is not None:
            result['AssetUuid'] = self.asset_uuid

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AssetUuid') is not None:
            self.asset_uuid = m.get('AssetUuid')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

