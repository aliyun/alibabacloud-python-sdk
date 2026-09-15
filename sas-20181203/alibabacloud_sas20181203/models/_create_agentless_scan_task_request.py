# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateAgentlessScanTaskRequest(DaraModel):
    def __init__(
        self,
        asset_selection_type: str = None,
        auto_delete_days: int = None,
        client_token: str = None,
        from_: str = None,
        region_id: str = None,
        release_after_scan: bool = None,
        resource_region_id: str = None,
        scan_data_disk: bool = None,
        target_type: int = None,
        targets: List[main_models.CreateAgentlessScanTaskRequestTargets] = None,
        uuid_list: List[str] = None,
    ):
        # The asset selection identifier.
        self.asset_selection_type = asset_selection_type
        # The image retention period, in days. This parameter takes effect only for host detection. It does not take effect for user snapshot detection or user custom image detection.
        self.auto_delete_days = auto_delete_days
        # The idempotency key.
        self.client_token = client_token
        # The source of the API call, which is used to collect statistics on scan task volume and scan data volume by source. If this parameter is not specified, the value is empty.
        self.from_ = from_
        # The region ID, which is usually automatically populated by the gateway.
        self.region_id = region_id
        # Specifies whether to enable the cost-saving mode. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.release_after_scan = release_after_scan
        # The region ID of the resource to be detected, such as cn-hangzhou.
        self.resource_region_id = resource_region_id
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
        # The list of targets for image security remediation. Each target specifies the source image, the region, the name of the remediated image, and the vulnerability identifiers to be fixed.
        self.targets = targets
        # The UUIDs of the assets to be detected.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the UUIDs of servers.
        self.uuid_list = uuid_list

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

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

        if self.from_ is not None:
            result['From'] = self.from_

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_after_scan is not None:
            result['ReleaseAfterScan'] = self.release_after_scan

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.scan_data_disk is not None:
            result['ScanDataDisk'] = self.scan_data_disk

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

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

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseAfterScan') is not None:
            self.release_after_scan = m.get('ReleaseAfterScan')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ScanDataDisk') is not None:
            self.scan_data_disk = m.get('ScanDataDisk')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.CreateAgentlessScanTaskRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

class CreateAgentlessScanTaskRequestTargets(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        origin_image_name: str = None,
        output_image_name: str = None,
        region_id: str = None,
        vulnerability_ids: List[str] = None,
    ):
        # The ID of the source ECS custom image to be remediated. The image must be located in the region specified by RegionId of this target.
        self.image_id = image_id
        # The name of the source ECS custom image to be remediated.
        self.origin_image_name = origin_image_name
        # The name of the ECS image generated after remediation.
        self.output_image_name = output_image_name
        # The region ID of the source image to be remediated, such as cn-hangzhou.
        self.region_id = region_id
        # The list of vulnerability identifiers to be fixed. At least one vulnerability identifier must be specified, and each identifier must be unique and non-empty.
        self.vulnerability_ids = vulnerability_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.origin_image_name is not None:
            result['OriginImageName'] = self.origin_image_name

        if self.output_image_name is not None:
            result['OutputImageName'] = self.output_image_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vulnerability_ids is not None:
            result['VulnerabilityIds'] = self.vulnerability_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OriginImageName') is not None:
            self.origin_image_name = m.get('OriginImageName')

        if m.get('OutputImageName') is not None:
            self.output_image_name = m.get('OutputImageName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VulnerabilityIds') is not None:
            self.vulnerability_ids = m.get('VulnerabilityIds')

        return self

