# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAgentlessScanTaskRequest(DaraModel):
    def __init__(
        self,
        asset_selection_type: str = None,
        auto_delete_days: int = None,
        client_token: str = None,
        region_id: str = None,
        release_after_scan: bool = None,
        scan_data_disk: bool = None,
        target_type: int = None,
        uuid_list: List[str] = None,
    ):
        # The asset selection identifier.
        self.asset_selection_type = asset_selection_type
        # The image retention period, in days. This parameter takes effect only for host detection and does not take effect for user snapshot detection or user custom image detection.
        self.auto_delete_days = auto_delete_days
        # The idempotency key.
        self.client_token = client_token
        # The region ID of the instance to query. Valid values:
        # 
        # - **cn-hangzhou** (default): China.
        # - **ap-southeast-1**: outside China.
        self.region_id = region_id
        # Specifies whether to enable the cost-saving mode. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.release_after_scan = release_after_scan
        # Specifies whether to detect data cloud disks. Valid values:
        # 
        # - **true**: Detected.
        # - **false**: Not detected.
        self.scan_data_disk = scan_data_disk
        # The target type. Valid values:
        # 
        # - **1**: Host detection - detection by snapshot.
        # - **2**: Host detection - detection by image.
        # - **3**: User snapshot detection.
        # - **2**: User custom image detection.
        # 
        # This parameter is required.
        self.target_type = target_type
        # The UUIDs of the assets to be detected.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the UUIDs of servers.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_selection_type is not None:
            result['AssetSelectionType'] = self.asset_selection_type

        if self.auto_delete_days is not None:
            result['AutoDeleteDays'] = self.auto_delete_days

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_after_scan is not None:
            result['ReleaseAfterScan'] = self.release_after_scan

        if self.scan_data_disk is not None:
            result['ScanDataDisk'] = self.scan_data_disk

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSelectionType') is not None:
            self.asset_selection_type = m.get('AssetSelectionType')

        if m.get('AutoDeleteDays') is not None:
            self.auto_delete_days = m.get('AutoDeleteDays')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseAfterScan') is not None:
            self.release_after_scan = m.get('ReleaseAfterScan')

        if m.get('ScanDataDisk') is not None:
            self.scan_data_disk = m.get('ScanDataDisk')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

