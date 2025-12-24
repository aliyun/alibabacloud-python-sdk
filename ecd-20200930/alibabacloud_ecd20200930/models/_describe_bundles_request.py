# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeBundlesRequest(DaraModel):
    def __init__(
        self,
        bundle_id: List[str] = None,
        bundle_type: str = None,
        check_stock: bool = None,
        cpu_count: int = None,
        desktop_type_family: str = None,
        fota_channel: str = None,
        from_desktop_group: bool = None,
        gpu_count: float = None,
        gpu_driver_type: str = None,
        image_id: List[str] = None,
        max_results: int = None,
        memory_size: int = None,
        next_token: str = None,
        os_type: str = None,
        protocol_type: str = None,
        region_id: str = None,
        scope: str = None,
        selected_bundle: bool = None,
        session_type: str = None,
        support_multi_session: bool = None,
        volume_encryption_enabled: bool = None,
    ):
        # The IDs of the cloud computer templates. You can specify 1 to 100 IDs.
        self.bundle_id = bundle_id
        # The type of the cloud computer template.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system template
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CUSTOM: custom template
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.bundle_type = bundle_type
        # Specifies whether to query the inventory status of the cloud computer instance type.
        self.check_stock = check_stock
        # The number of vCPUs contained in the cloud computer instance type.
        self.cpu_count = cpu_count
        # The instance family of the cloud computers.
        # 
        # Valid values:
        # 
        # *   eds.graphics: graphical instance families
        # *   eds.hf: instance families with high clock speeds
        # *   eds.general: general-purpose instance families
        self.desktop_type_family = desktop_type_family
        # >  This parameter is not available for public use.
        self.fota_channel = fota_channel
        # Specifies whether the cloud computers in the template belong to a cloud computer pool.
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
        self.from_desktop_group = from_desktop_group
        # The number of GPUs contained in the cloud computer instance type.
        self.gpu_count = gpu_count
        # The GPU driver type.
        # 
        # Valid values:
        # 
        # *   T4
        # *   A10
        # *   G28
        # *   G39
        self.gpu_driver_type = gpu_driver_type
        # The image IDs.
        self.image_id = image_id
        # The number of entries to return on each page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The memory size of the cloud computer instance type. Unit: GiB.
        self.memory_size = memory_size
        # The token that is used to start the next query.
        self.next_token = next_token
        # The type of the OS.
        # 
        # Valid values:
        # 
        # *   Linux
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.os_type = os_type
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX) protocol
        # *   ASP: in-house Adaptive Streaming Protocol (ASP) (recommend)
        self.protocol_type = protocol_type
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The scenario to use the image.
        self.scope = scope
        # The desktop template that is selected based on specific criteria.
        self.selected_bundle = selected_bundle
        # The type of the session. Valide values:
        # 
        # - SingleSession
        # - MultipleSession
        self.session_type = session_type
        # Specifies whether to return multi-session cloud computer templates. Default value: false.
        self.support_multi_session = support_multi_session
        # Specifies whether to enable disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type

        if self.check_stock is not None:
            result['CheckStock'] = self.check_stock

        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.desktop_type_family is not None:
            result['DesktopTypeFamily'] = self.desktop_type_family

        if self.fota_channel is not None:
            result['FotaChannel'] = self.fota_channel

        if self.from_desktop_group is not None:
            result['FromDesktopGroup'] = self.from_desktop_group

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_driver_type is not None:
            result['GpuDriverType'] = self.gpu_driver_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.selected_bundle is not None:
            result['SelectedBundle'] = self.selected_bundle

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.support_multi_session is not None:
            result['SupportMultiSession'] = self.support_multi_session

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')

        if m.get('CheckStock') is not None:
            self.check_stock = m.get('CheckStock')

        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('DesktopTypeFamily') is not None:
            self.desktop_type_family = m.get('DesktopTypeFamily')

        if m.get('FotaChannel') is not None:
            self.fota_channel = m.get('FotaChannel')

        if m.get('FromDesktopGroup') is not None:
            self.from_desktop_group = m.get('FromDesktopGroup')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuDriverType') is not None:
            self.gpu_driver_type = m.get('GpuDriverType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SelectedBundle') is not None:
            self.selected_bundle = m.get('SelectedBundle')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('SupportMultiSession') is not None:
            self.support_multi_session = m.get('SupportMultiSession')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        return self

