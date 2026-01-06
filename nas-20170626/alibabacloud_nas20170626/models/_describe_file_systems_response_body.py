# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFileSystemsResponseBody(DaraModel):
    def __init__(
        self,
        file_systems: main_models.DescribeFileSystemsResponseBodyFileSystems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The file system list.
        self.file_systems = file_systems
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of file systems.
        self.total_count = total_count

    def validate(self):
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystems') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m.get('FileSystems'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFileSystemsResponseBodyFileSystems(DaraModel):
    def __init__(
        self,
        file_system: List[main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystem] = None,
    ):
        self.file_system = file_system

    def validate(self):
        if self.file_system:
            for v1 in self.file_system:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileSystem'] = []
        if self.file_system is not None:
            for k1 in self.file_system:
                result['FileSystem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k1 in m.get('FileSystem'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystem(DaraModel):
    def __init__(
        self,
        access_point_count: str = None,
        auto_snapshot_policy_id: str = None,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        encrypt_type: int = None,
        expired_time: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        kmskey_id: str = None,
        ldap: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap = None,
        metered_archive_size: int = None,
        metered_iasize: int = None,
        metered_size: int = None,
        mount_targets: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets = None,
        options: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemOptions = None,
        packages: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages = None,
        protocol_type: str = None,
        quorum_vsw_id: str = None,
        redundancy_type: str = None,
        redundancy_vswitch_ids: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemRedundancyVSwitchIds = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        storage_type: str = None,
        supported_features: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures = None,
        tags: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemTags = None,
        version: str = None,
        vpc_id: str = None,
        vsc_target: str = None,
        vsw_ids: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemVswIds = None,
        zone_id: str = None,
    ):
        # Number of access points.
        self.access_point_count = access_point_count
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The bandwidth of the file system.
        # 
        # Unit: MB/s. This parameter is unavailable for General-purpose NAS file systems.
        self.bandwidth = bandwidth
        # The capacity of the file system.
        # 
        # Unit: GiB.
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # 
        # *   Subscription
        # *   PayAsYouGo
        # *   Package: storage plan
        self.charge_type = charge_type
        # The time when the file system was created.
        self.create_time = create_time
        # The description of the file system.
        self.description = description
        # Indicates whether the data in the file system is encrypted.
        # 
        # Valid values:
        # 
        # *   0: The data in the file system is not encrypted.
        # *   1: A NAS-managed key is used to encrypt the data in the file system.
        # *   2: A KMS-managed key is used to encrypt the data in the file system.
        self.encrypt_type = encrypt_type
        # The time when the file system expires.
        self.expired_time = expired_time
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The file system type.
        # 
        # The following information is displayed:
        # 
        # *   standard: General-purpose NAS file system.
        # *   extreme: Extreme NAS file system.
        # *   cpfs: CPFS file system.
        self.file_system_type = file_system_type
        # The ID of the key that is managed by Key Management Service (KMS).
        self.kmskey_id = kmskey_id
        # The Lightweight Directory Access Protocol (LDAP) configurations.
        # 
        # This parameter is available only for CPFS file systems.
        self.ldap = ldap
        # Archive storage usage.
        # 
        # Unit: Byte.
        self.metered_archive_size = metered_archive_size
        # The storage usage of the Infrequent Access (IA) storage medium.
        # 
        # Unit: bytes.
        self.metered_iasize = metered_iasize
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour. Unit: bytes.
        self.metered_size = metered_size
        # The queried mount targets.
        self.mount_targets = mount_targets
        # The options.
        self.options = options
        # The information about storage plans.
        self.packages = packages
        # The protocol type of the file system.
        # 
        # The following information is displayed:
        # 
        # *   NFS: Network File System.
        # *   SMB: Server Message Block.
        # *   cpfs: The protocol type supported by the CPFS file system.
        self.protocol_type = protocol_type
        # The vSwitch ID.
        self.quorum_vsw_id = quorum_vsw_id
        self.redundancy_type = redundancy_type
        self.redundancy_vswitch_ids = redundancy_vswitch_ids
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the file system. Valid values:
        # - Pending: The file system is being created or modified.
        # - Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state.
        # - Stopped: The file system is unavailable.
        # - Extending: The file system is being scaled up.
        # - Stopping: The file system is being stopped.
        # - Deleting: The file system is being deleted.
        self.status = status
        # The type of the storage.
        # 
        # The following information is displayed:
        # 
        # *   Valid values for General-purpose NAS file systems: Capacity, Performance, and Premium
        # *   Valid values for Extreme NAS file systems: standard and advance
        # *   Valid values for Cloud Parallel File Storage (CPFS) file systems: advance_100 (100 MB/s/TiB baseline) and advance_200 (200 MB/s/TiB baseline)
        self.storage_type = storage_type
        # The features that are supported by the file system.
        self.supported_features = supported_features
        # The tags that are attached to the file system.
        self.tags = tags
        # The version number of the file system.
        # 
        # This parameter is available only for Extreme NAS file systems and CPFS file systems.
        self.version = version
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # >  This parameter is not publicly available.
        self.vsc_target = vsc_target
        # The information about vSwitch.
        self.vsw_ids = vsw_ids
        # The ID of the zone where the file system resides.
        self.zone_id = zone_id

    def validate(self):
        if self.ldap:
            self.ldap.validate()
        if self.mount_targets:
            self.mount_targets.validate()
        if self.options:
            self.options.validate()
        if self.packages:
            self.packages.validate()
        if self.redundancy_vswitch_ids:
            self.redundancy_vswitch_ids.validate()
        if self.supported_features:
            self.supported_features.validate()
        if self.tags:
            self.tags.validate()
        if self.vsw_ids:
            self.vsw_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_count is not None:
            result['AccessPointCount'] = self.access_point_count

        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.ldap is not None:
            result['Ldap'] = self.ldap.to_map()

        if self.metered_archive_size is not None:
            result['MeteredArchiveSize'] = self.metered_archive_size

        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize

        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size

        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()

        if self.options is not None:
            result['Options'] = self.options.to_map()

        if self.packages is not None:
            result['Packages'] = self.packages.to_map()

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.quorum_vsw_id is not None:
            result['QuorumVswId'] = self.quorum_vsw_id

        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type

        if self.redundancy_vswitch_ids is not None:
            result['RedundancyVSwitchIds'] = self.redundancy_vswitch_ids.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.supported_features is not None:
            result['SupportedFeatures'] = self.supported_features.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vsc_target is not None:
            result['VscTarget'] = self.vsc_target

        if self.vsw_ids is not None:
            result['VswIds'] = self.vsw_ids.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointCount') is not None:
            self.access_point_count = m.get('AccessPointCount')

        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('Ldap') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap()
            self.ldap = temp_model.from_map(m.get('Ldap'))

        if m.get('MeteredArchiveSize') is not None:
            self.metered_archive_size = m.get('MeteredArchiveSize')

        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')

        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')

        if m.get('MountTargets') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets()
            self.mount_targets = temp_model.from_map(m.get('MountTargets'))

        if m.get('Options') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemOptions()
            self.options = temp_model.from_map(m.get('Options'))

        if m.get('Packages') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m.get('Packages'))

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('QuorumVswId') is not None:
            self.quorum_vsw_id = m.get('QuorumVswId')

        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')

        if m.get('RedundancyVSwitchIds') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemRedundancyVSwitchIds()
            self.redundancy_vswitch_ids = temp_model.from_map(m.get('RedundancyVSwitchIds'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SupportedFeatures') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures()
            self.supported_features = temp_model.from_map(m.get('SupportedFeatures'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VscTarget') is not None:
            self.vsc_target = m.get('VscTarget')

        if m.get('VswIds') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemVswIds()
            self.vsw_ids = temp_model.from_map(m.get('VswIds'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemVswIds(DaraModel):
    def __init__(
        self,
        vsw_id: List[str] = None,
    ):
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures(DaraModel):
    def __init__(
        self,
        supported_feature: List[str] = None,
    ):
        self.supported_feature = supported_feature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_feature is not None:
            result['SupportedFeature'] = self.supported_feature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedFeature') is not None:
            self.supported_feature = m.get('SupportedFeature')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemRedundancyVSwitchIds(DaraModel):
    def __init__(
        self,
        redundancy_vswitch_id: List[str] = None,
    ):
        self.redundancy_vswitch_id = redundancy_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.redundancy_vswitch_id is not None:
            result['RedundancyVSwitchId'] = self.redundancy_vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedundancyVSwitchId') is not None:
            self.redundancy_vswitch_id = m.get('RedundancyVSwitchId')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages(DaraModel):
    def __init__(
        self,
        package: List[main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for v1 in self.package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Package'] = []
        if self.package is not None:
            for k1 in self.package:
                result['Package'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k1 in m.get('Package'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage(DaraModel):
    def __init__(
        self,
        expired_time: str = None,
        package_id: str = None,
        package_type: str = None,
        size: int = None,
        start_time: str = None,
    ):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time
        # The ID of the storage plan.
        self.package_id = package_id
        # The type of the storage plan.
        # 
        # Valid values:
        # 
        # *   ssd: The storage plan for Performance NAS file systems.
        # *   hybrid: The storage plan for Capacity NAS file systems.
        self.package_type = package_type
        # The capacity of the storage plan. Unit: bytes.
        self.size = size
        # The start time of the validity period for the storage plan.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemOptions(DaraModel):
    def __init__(
        self,
        enable_oplock: bool = None,
    ):
        # Specifies whether to enable the oplock feature. Valid values:
        # 
        # *   true: enables the feature.
        # *   false: disables the feature.
        # 
        # >  Only Server Message Block (SMB) file systems support this feature.
        self.enable_oplock = enable_oplock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_oplock is not None:
            result['EnableOplock'] = self.enable_oplock

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOplock') is not None:
            self.enable_oplock = m.get('EnableOplock')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets(DaraModel):
    def __init__(
        self,
        mount_target: List[main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget] = None,
    ):
        self.mount_target = mount_target

    def validate(self):
        if self.mount_target:
            for v1 in self.mount_target:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k1 in self.mount_target:
                result['MountTarget'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k1 in m.get('MountTarget'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        client_master_nodes: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes = None,
        dual_stack_mount_target_domain: str = None,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        tags: main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The name of the permission group that is attached to the mount target.
        self.access_group_name = access_group_name
        # The information about client management nodes.
        # 
        # This parameter is available only for CPFS file systems.
        self.client_master_nodes = client_master_nodes
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The network type. Valid value: vpc.
        self.network_type = network_type
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active
        # *   Inactive
        # *   Pending
        # *   Deleting
        # *   Hibernating
        # *   Hibernated
        self.status = status
        # The tags that are attached to the mount target.
        self.tags = tags
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vsw_id = vsw_id

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()

        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('ClientMasterNodes') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m.get('ClientMasterNodes'))

        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes(DaraModel):
    def __init__(
        self,
        client_master_node: List[main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode] = None,
    ):
        self.client_master_node = client_master_node

    def validate(self):
        if self.client_master_node:
            for v1 in self.client_master_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k1 in self.client_master_node:
                result['ClientMasterNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k1 in m.get('ClientMasterNode'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode(DaraModel):
    def __init__(
        self,
        default_passwd: str = None,
        ecs_id: str = None,
        ecs_ip: str = None,
    ):
        # The default logon password of the ECS instance on the client management node.
        self.default_passwd = default_passwd
        # The ID of the ECS instance on the client management node.
        self.ecs_id = ecs_id
        # The IP address of the ECS instance on the client management node.
        self.ecs_ip = ecs_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd

        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id

        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')

        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')

        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')

        return self

class DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap(DaraModel):
    def __init__(
        self,
        bind_dn: str = None,
        search_base: str = None,
        uri: str = None,
    ):
        # An LDAP entry.
        self.bind_dn = bind_dn
        # An LDAP search base.
        self.search_base = search_base
        # An LDAP URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn

        if self.search_base is not None:
            result['SearchBase'] = self.search_base

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')

        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

