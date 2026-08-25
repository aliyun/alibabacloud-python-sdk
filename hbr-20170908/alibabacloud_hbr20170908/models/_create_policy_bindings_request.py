# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class CreatePolicyBindingsRequest(DaraModel):
    def __init__(
        self,
        policy_binding_list: List[main_models.CreatePolicyBindingsRequestPolicyBindingList] = None,
        policy_id: str = None,
    ):
        # The list of policy bindings.
        self.policy_binding_list = policy_binding_list
        # The policy ID.
        self.policy_id = policy_id

    def validate(self):
        if self.policy_binding_list:
            for v1 in self.policy_binding_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolicyBindingList'] = []
        if self.policy_binding_list is not None:
            for k1 in self.policy_binding_list:
                result['PolicyBindingList'].append(k1.to_map() if k1 else None)

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_binding_list = []
        if m.get('PolicyBindingList') is not None:
            for k1 in m.get('PolicyBindingList'):
                temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingList()
                self.policy_binding_list.append(temp_model.from_map(k1))

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

class CreatePolicyBindingsRequestPolicyBindingList(DaraModel):
    def __init__(
        self,
        advanced_options: main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        disabled: str = None,
        exclude: str = None,
        include: str = None,
        policy_binding_description: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
    ):
        # The advanced options.
        self.advanced_options = advanced_options
        # The RAM role name created in the source account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # The cross-account backup type. Default value: SELF_ACCOUNT. Valid values: 
        # - **SELF_ACCOUNT**: Backup within the same account.
        # - **CROSS_ACCOUNT**: Cross-account backup.
        self.cross_account_type = cross_account_type
        # The Alibaba Cloud UID of the source account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The data source ID. The value has different meanings depending on the **SourceType** field:
        # - **UDM_ECS**: The ECS instance ID.
        # - **OSS**: The OSS bucket name.
        # - **NAS**: The Alibaba Cloud NAS file system ID.
        # - **COMMON_NAS**: The on-premises NAS instance ID.
        # - **ECS_FILE**: The ECS instance ID.
        # - **File**: The Cloud Backup client ID.
        # - **COMMON_FILE_SYSTEM**: The CPFS backup data source ID.
        self.data_source_id = data_source_id
        # Specifies whether the policy is suspended for this data source.
        # - true: Suspended.
        # - false: Not suspended.
        self.disabled = disabled
        # This parameter can be configured when **SourceType** is set to **ECS_FILE**, **File**, **NAS**, **COMMON_NAS**, or **COMMON_FILE_SYSTEM**. Specifies the file types to exclude from the backup. All files of these types are not backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter can be configured when **SourceType** is set to **ECS_FILE**, **File**, **NAS**, **COMMON_NAS**, or **COMMON_FILE_SYSTEM**. Specifies the file types to include in the backup. All files of these types are backed up. The value can be up to 255 characters in length.
        self.include = include
        # The description of the policy binding.
        self.policy_binding_description = policy_binding_description
        # The value has different meanings depending on the SourceType value:
        # - **OSS**: The prefix to back up. If not specified, the entire bucket root directory is backed up. Only a single prefix is supported. To back up /backup, specify /backup.
        # - **ECS_FILE**: The file directories to back up. If not specified, all directories are backed up. Multiple directories are supported. To back up files under /a and /b, specify ["/a", "/b"].
        # - **File**: The file directories to back up. If not specified, all directories are backed up. Multiple directories are supported. To back up files under /a and /b, specify ["/a", "/b"].
        # - **COMMON_FILE_SYSTEM**: Required. The source paths to back up. Multiple paths are supported. To back up /a and /b, specify ["/a", "/b"]. To back up the root path, specify ["/"].
        # - **COMMON_NAS**: Required. The source path to back up. Only a single path is supported. To back up /a, specify ["/a"]. To back up the root path, specify ["/"].
        # - **OTS**: The list of data tables to back up. If not specified, all data tables are backed up. Multiple data tables are supported. To back up tables a and b, specify ["a", "b"].
        self.source = source
        # The data source type. Valid values:
        # - **UDM_ECS**: ECS full server backup.
        # - **OSS**: OSS backup.
        # - **NAS**: Alibaba Cloud NAS backup.
        # - **COMMON_NAS**: On-premises NAS backup.
        # - **ECS_FILE**: ECS File Backup Essential Edition.
        # - **File**: On-premises file backup.
        # - **COMMON_FILE_SYSTEM**: CPFS backup.
        # - **OTS**: Tablestore backup.
        self.source_type = source_type
        # This parameter is required only when **SourceType** is set to **ECS_FILE** or **File**. Specifies the backup traffic control. The format is `{start}{end}{bandwidth}`. Multiple traffic control configurations are separated by delimiters, and the time ranges must not overlap.
        # 
        # - **start**: The start hour.
        # - **end**: The end hour.
        # - **bandwidth**: The rate limit, in KB/s.
        self.speed_limit = speed_limit

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.include is not None:
            result['Include'] = self.include

        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions()
            self.advanced_options = temp_model.from_map(m.get('AdvancedOptions'))

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        return self

class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions(DaraModel):
    def __init__(
        self,
        common_file_system_detail: main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail = None,
        common_nas_detail: main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail = None,
        file_detail: main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail = None,
        oss_detail: main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail = None,
        udm_detail: main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail = None,
    ):
        # The advanced options for CPFS backup.
        self.common_file_system_detail = common_file_system_detail
        # The advanced options for on-premises NAS backup.
        self.common_nas_detail = common_nas_detail
        # The advanced options for file backup.
        self.file_detail = file_detail
        # The advanced options for OSS backup.
        self.oss_detail = oss_detail
        # The advanced options for ECS full server backup.
        self.udm_detail = udm_detail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.common_nas_detail:
            self.common_nas_detail.validate()
        if self.file_detail:
            self.file_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()

        if self.common_nas_detail is not None:
            result['CommonNasDetail'] = self.common_nas_detail.to_map()

        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()

        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()

        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m.get('CommonFileSystemDetail'))

        if m.get('CommonNasDetail') is not None:
            temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail()
            self.common_nas_detail = temp_model.from_map(m.get('CommonNasDetail'))

        if m.get('FileDetail') is not None:
            temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail()
            self.file_detail = temp_model.from_map(m.get('FileDetail'))

        if m.get('OssDetail') is not None:
            temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m.get('OssDetail'))

        if m.get('UdmDetail') is not None:
            temp_model = main_models.CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m.get('UdmDetail'))

        return self

class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail(DaraModel):
    def __init__(
        self,
        app_consistent: bool = None,
        disk_id_list: List[str] = None,
        enable_fs_freeze: bool = None,
        enable_writers: bool = None,
        exclude_disk_id_list: List[str] = None,
        post_script_path: str = None,
        pre_script_path: str = None,
        ram_role_name: str = None,
        snapshot_group: bool = None,
        timeout_in_seconds: int = None,
    ):
        # Specifies whether to create an application-consistent snapshot. Application-consistent snapshots are supported only when all cloud disk types are ESSD.
        self.app_consistent = app_consistent
        # The list of cloud disk IDs that need to be protected. Leave this value empty to protect all cloud disks.
        self.disk_id_list = disk_id_list
        # This parameter is required only when **AppConsistent** is set to **true**. Specifies whether to use the Linux FsFreeze mechanism to ensure the file system is in read consistency before creating an application-consistent snapshot. Default value: true.
        self.enable_fs_freeze = enable_fs_freeze
        # This parameter is required only when **AppConsistent** is set to **true**. Specifies whether to create an application-consistent snapshot:
        # - true: Creates an application-consistent snapshot.
        # - false: Creates a file system-consistent snapshot.
        # 
        # Default value: true.
        self.enable_writers = enable_writers
        # The list of cloud disk IDs that do not need to be protected. This parameter is ignored when DiskIdList is not empty.
        self.exclude_disk_id_list = exclude_disk_id_list
        # This parameter is required only when **AppConsistent** is set to **true**. The path of the post-thaw script to run after creating an application-consistent snapshot.
        self.post_script_path = post_script_path
        # This parameter is required only when **AppConsistent** is set to **true**. The path of the pre-freeze script to run before creating an application-consistent snapshot.
        self.pre_script_path = pre_script_path
        # This parameter is required only when **AppConsistent** is set to **true**. The RAM role name required for creating application-consistent snapshots.
        self.ram_role_name = ram_role_name
        # Specifies whether to create a snapshot-consistent group. Snapshot-consistent groups are supported only when all cloud disk types are ESSD.
        self.snapshot_group = snapshot_group
        # This parameter is required only when **AppConsistent** is set to **true**. The I/O freeze timeout period, in seconds. Default value: 30.
        self.timeout_in_seconds = timeout_in_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent

        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list

        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze

        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers

        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list

        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path

        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group

        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')

        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')

        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')

        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')

        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')

        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')

        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')

        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')

        return self

class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail(DaraModel):
    def __init__(
        self,
        ignore_archive_object: bool = None,
        inventory_cleanup_policy: str = None,
        inventory_id: str = None,
    ):
        # Specifies whether to exclude archive objects from job statistics and failed file lists.
        self.ignore_archive_object = ignore_archive_object
        # Specifies whether to delete inventory files after backup. This parameter takes effect only when OSS inventory is used. Valid values:
        # - **NO_CLEANUP**: Do not delete.
        # - **DELETE_CURRENT**: Delete the current file.
        # - **DELETE_CURRENT_AND_PREVIOUS**: Delete all files.
        self.inventory_cleanup_policy = inventory_cleanup_policy
        # The OSS inventory name. When this value is not empty, the OSS inventory is used for performance optimization.
        # - Using an inventory is recommended for backing up more than 100 million OSS objects to improve incremental performance. Storage fees generated by inventory files are charged separately by OSS.
        # - OSS inventory files take time to generate. Backup jobs may fail before the inventory files are generated. Wait for the next backup cycle.
        self.inventory_id = inventory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_archive_object is not None:
            result['IgnoreArchiveObject'] = self.ignore_archive_object

        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy

        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreArchiveObject') is not None:
            self.ignore_archive_object = m.get('IgnoreArchiveObject')

        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')

        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')

        return self

class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail(DaraModel):
    def __init__(
        self,
        adv_policy: bool = None,
        use_vss: bool = None,
    ):
        # Specifies whether to use an advanced policy. Valid values:
        # - **true**: Use.
        # - **false**: Do not use.
        self.adv_policy = adv_policy
        # Specifies whether to enable the Volume Shadow Copy Service (VSS) feature (Windows). Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.use_vss = use_vss

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adv_policy is not None:
            result['AdvPolicy'] = self.adv_policy

        if self.use_vss is not None:
            result['UseVSS'] = self.use_vss

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvPolicy') is not None:
            self.adv_policy = m.get('AdvPolicy')

        if m.get('UseVSS') is not None:
            self.use_vss = m.get('UseVSS')

        return self

class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The backup client group ID. On-premises NAS backup selects a client from the backup client group to perform the backup.
        self.cluster_id = cluster_id
        # The sub-task slice size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether to switch to a full backup when an incremental backup fails. Valid values:
        # - **true**: Switch to a full backup on failure.
        # - **false**: Do not switch to a full backup on failure.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size

        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')

        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')

        return self

class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail(DaraModel):
    def __init__(
        self,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The sub-task slice size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether to switch to a full backup when an incremental backup fails. Valid values:
        # - **true**: Switch to a full backup on failure.
        # - **false**: Do not switch to a full backup on failure.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size

        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')

        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')

        return self

