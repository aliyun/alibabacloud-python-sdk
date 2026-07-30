# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeNASFileSystemsResponseBody(DaraModel):
    def __init__(
        self,
        file_systems: List[main_models.DescribeNASFileSystemsResponseBodyFileSystems] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The NAS file system information.
        self.file_systems = file_systems
        # The pagination token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.file_systems:
            for v1 in self.file_systems:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k1 in self.file_systems:
                result['FileSystems'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k1 in m.get('FileSystems'):
                temp_model = main_models.DescribeNASFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNASFileSystemsResponseBodyFileSystems(DaraModel):
    def __init__(
        self,
        allow_operate_user_drive: bool = None,
        app_instance_groups: List[main_models.DescribeNASFileSystemsResponseBodyFileSystemsAppInstanceGroups] = None,
        capacity: int = None,
        create_time: str = None,
        description: str = None,
        desktop_groups: List[main_models.DescribeNASFileSystemsResponseBodyFileSystemsDesktopGroups] = None,
        encryption_enabled: bool = None,
        file_system_id: str = None,
        file_system_name: str = None,
        file_system_status: str = None,
        file_system_type: str = None,
        metered_size: int = None,
        mount_target_domain: str = None,
        mount_target_status: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_sites: List[main_models.DescribeNASFileSystemsResponseBodyFileSystemsOfficeSites] = None,
        product_type: str = None,
        profile_compatible: bool = None,
        protocol_type: str = None,
        region_id: str = None,
        scene: str = None,
        size_quota: int = None,
        storage_type: str = None,
        support_acl: bool = None,
        zone_id: str = None,
    ):
        # > This field is not publicly available.
        self.allow_operate_user_drive = allow_operate_user_drive
        # The list of cloud application delivery group objects bound to the UPM-supported NAS file system.
        self.app_instance_groups = app_instance_groups
        # The total capacity of the NAS file system. Unit: GiB.
        # 
        # - If the storage type is Capacity, the capacity is fixed at 10 PiB (10485760 GiB).
        # - If the storage type is Performance, the capacity is fixed at 1 PiB (1048576 GiB).
        self.capacity = capacity
        # The time when the NAS file system was created.
        self.create_time = create_time
        # The NAS file system description.
        self.description = description
        # The list of shared cloud computer objects bound to the UPM-supported NAS file system.
        self.desktop_groups = desktop_groups
        # Indicates whether disk encryption is enabled.
        self.encryption_enabled = encryption_enabled
        # The NAS file system ID.
        self.file_system_id = file_system_id
        # The NAS file system name.
        self.file_system_name = file_system_name
        # The NAS file system status.
        self.file_system_status = file_system_status
        # The type of the NAS file system. Currently, only the general-purpose type is supported, which is `standard`.
        self.file_system_type = file_system_type
        # The used capacity of the NAS file system. Unit: bytes.
        self.metered_size = metered_size
        # The mount target domain name.
        self.mount_target_domain = mount_target_domain
        # The mount target status.
        self.mount_target_status = mount_target_status
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The list of office networks.
        self.office_sites = office_sites
        self.product_type = product_type
        # Indicates whether the User Profile Management (UPM) feature is supported.
        self.profile_compatible = profile_compatible
        self.protocol_type = protocol_type
        # The region ID.
        self.region_id = region_id
        # The storage mode of the NAS file system.
        self.scene = scene
        self.size_quota = size_quota
        # The storage type of the NAS file system.
        self.storage_type = storage_type
        # Indicates whether the SMB ACL feature is supported.
        self.support_acl = support_acl
        # The zone.
        self.zone_id = zone_id

    def validate(self):
        if self.app_instance_groups:
            for v1 in self.app_instance_groups:
                 if v1:
                    v1.validate()
        if self.desktop_groups:
            for v1 in self.desktop_groups:
                 if v1:
                    v1.validate()
        if self.office_sites:
            for v1 in self.office_sites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_operate_user_drive is not None:
            result['AllowOperateUserDrive'] = self.allow_operate_user_drive

        result['AppInstanceGroups'] = []
        if self.app_instance_groups is not None:
            for k1 in self.app_instance_groups:
                result['AppInstanceGroups'].append(k1.to_map() if k1 else None)

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['DesktopGroups'] = []
        if self.desktop_groups is not None:
            for k1 in self.desktop_groups:
                result['DesktopGroups'].append(k1.to_map() if k1 else None)

        if self.encryption_enabled is not None:
            result['EncryptionEnabled'] = self.encryption_enabled

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.file_system_status is not None:
            result['FileSystemStatus'] = self.file_system_status

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.mount_target_status is not None:
            result['MountTargetStatus'] = self.mount_target_status

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k1 in self.office_sites:
                result['OfficeSites'].append(k1.to_map() if k1 else None)

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.profile_compatible is not None:
            result['ProfileCompatible'] = self.profile_compatible

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.size_quota is not None:
            result['SizeQuota'] = self.size_quota

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.support_acl is not None:
            result['SupportAcl'] = self.support_acl

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowOperateUserDrive') is not None:
            self.allow_operate_user_drive = m.get('AllowOperateUserDrive')

        self.app_instance_groups = []
        if m.get('AppInstanceGroups') is not None:
            for k1 in m.get('AppInstanceGroups'):
                temp_model = main_models.DescribeNASFileSystemsResponseBodyFileSystemsAppInstanceGroups()
                self.app_instance_groups.append(temp_model.from_map(k1))

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.desktop_groups = []
        if m.get('DesktopGroups') is not None:
            for k1 in m.get('DesktopGroups'):
                temp_model = main_models.DescribeNASFileSystemsResponseBodyFileSystemsDesktopGroups()
                self.desktop_groups.append(temp_model.from_map(k1))

        if m.get('EncryptionEnabled') is not None:
            self.encryption_enabled = m.get('EncryptionEnabled')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('FileSystemStatus') is not None:
            self.file_system_status = m.get('FileSystemStatus')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('MountTargetStatus') is not None:
            self.mount_target_status = m.get('MountTargetStatus')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k1 in m.get('OfficeSites'):
                temp_model = main_models.DescribeNASFileSystemsResponseBodyFileSystemsOfficeSites()
                self.office_sites.append(temp_model.from_map(k1))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProfileCompatible') is not None:
            self.profile_compatible = m.get('ProfileCompatible')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SizeQuota') is not None:
            self.size_quota = m.get('SizeQuota')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SupportAcl') is not None:
            self.support_acl = m.get('SupportAcl')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeNASFileSystemsResponseBodyFileSystemsOfficeSites(DaraModel):
    def __init__(
        self,
        office_site_id: str = None,
        office_site_name: str = None,
    ):
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        return self

class DescribeNASFileSystemsResponseBodyFileSystemsDesktopGroups(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
    ):
        # The shared cloud computer ID.
        self.desktop_group_id = desktop_group_id
        # The shared cloud computer name.
        self.desktop_group_name = desktop_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        return self

class DescribeNASFileSystemsResponseBodyFileSystemsAppInstanceGroups(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
    ):
        # The delivery group ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name.
        self.app_instance_group_name = app_instance_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        return self

