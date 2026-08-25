# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribePolicyBindingsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        policy_bindings: List[main_models.DescribePolicyBindingsResponseBodyPolicyBindings] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. 200 indicates success.
        self.code = code
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The returned message. "successful" is returned for success. An error message is returned for failure.
        self.message = message
        # The token required to obtain the next page of policy-data source bindings.
        self.next_token = next_token
        # The list of policy bindings.
        self.policy_bindings = policy_bindings
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: Successful.
        # - false: Failed.
        self.success = success
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.policy_bindings:
            for v1 in self.policy_bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PolicyBindings'] = []
        if self.policy_bindings is not None:
            for k1 in self.policy_bindings:
                result['PolicyBindings'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policy_bindings = []
        if m.get('PolicyBindings') is not None:
            for k1 in m.get('PolicyBindings'):
                temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindings()
                self.policy_bindings.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePolicyBindingsResponseBodyPolicyBindings(DaraModel):
    def __init__(
        self,
        advanced_options: main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions = None,
        created_by_tag: bool = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        disabled: bool = None,
        exclude: str = None,
        hit_tags: List[main_models.DescribePolicyBindingsResponseBodyPolicyBindingsHitTags] = None,
        include: str = None,
        policy_binding_description: str = None,
        policy_binding_id: str = None,
        policy_id: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
        updated_time: int = None,
    ):
        # The advanced options.
        self.advanced_options = advanced_options
        # Indicates whether the resource is automatically associated through a backup policy resource tag.
        self.created_by_tag = created_by_tag
        # The creation time. UNIX timestamp, in seconds.
        self.created_time = created_time
        # The RAM role name created in the source account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # The cross-account backup type. Valid values: 
        # - SELF_ACCOUNT: backup within the current account.
        # - CROSS_ACCOUNT: cross-account backup.
        self.cross_account_type = cross_account_type
        # The ID of the source account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The data source ID.
        self.data_source_id = data_source_id
        # Indicates whether the policy is effective for the data source.
        # - true: paused.
        # - false: not paused.
        self.disabled = disabled
        # This parameter is required only when **SourceType** is set to **ECS_FILE** or **File**. Specifies the file types to exclude from backup. All files of these types are not backed up. Maximum of 255 characters.
        self.exclude = exclude
        # The matched tag rules.
        self.hit_tags = hit_tags
        # This parameter is required only when **SourceType** is set to **ECS_FILE** or **File**. Specifies the file types to back up. All files of these types are backed up. Maximum of 255 characters.
        self.include = include
        # The description of the policy binding.
        self.policy_binding_description = policy_binding_description
        # The policy binding ID.
        self.policy_binding_id = policy_binding_id
        # The policy ID.
        self.policy_id = policy_id
        # - If SourceType is set to **OSS**, this parameter specifies the prefix to back up. If not specified, the entire Bucket root directory is backed up.
        # - If SourceType is set to **ECS_FILE** or **File**, this parameter specifies the file directory to back up. If not specified, all directories are backed up.
        self.source = source
        # The data source type. Valid values:
        # - **UDM_ECS**: ECS instance backup.
        # - **OSS**: OSS backup.
        # - **NAS**: Alibaba Cloud NAS backup.
        # - **COMMON_NAS**: On-premises NAS backup.
        # - **ECS_FILE**: ECS File Backup Essential Edition.
        # - **File**: On-premises file backup.
        # - **COMMON_FILE_SYSTEM**: CPFS backup.
        # - **OTS**: Tablestore backup.
        self.source_type = source_type
        # This parameter is required only when **SourceType** is set to **ECS_FILE** or **File**. Specifies the backup traffic control. Format: `{start}{end}{bandwidth}`. Multiple traffic control configurations are separated by delimiters, and configuration times cannot overlap.
        # 
        # - **start**: start hour.
        # - **end**: end hour.
        # - **bandwidth**: rate limit, in KB/s.
        self.speed_limit = speed_limit
        # The update time. UNIX timestamp, in seconds.
        self.updated_time = updated_time

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()
        if self.hit_tags:
            for v1 in self.hit_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()

        if self.created_by_tag is not None:
            result['CreatedByTag'] = self.created_by_tag

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

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

        result['HitTags'] = []
        if self.hit_tags is not None:
            for k1 in self.hit_tags:
                result['HitTags'].append(k1.to_map() if k1 else None)

        if self.include is not None:
            result['Include'] = self.include

        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description

        if self.policy_binding_id is not None:
            result['PolicyBindingId'] = self.policy_binding_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions()
            self.advanced_options = temp_model.from_map(m.get('AdvancedOptions'))

        if m.get('CreatedByTag') is not None:
            self.created_by_tag = m.get('CreatedByTag')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

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

        self.hit_tags = []
        if m.get('HitTags') is not None:
            for k1 in m.get('HitTags'):
                temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsHitTags()
                self.hit_tags.append(temp_model.from_map(k1))

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')

        if m.get('PolicyBindingId') is not None:
            self.policy_binding_id = m.get('PolicyBindingId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class DescribePolicyBindingsResponseBodyPolicyBindingsHitTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag matching rule.
        # - **EQUAL**: Matches both the tag key and tag value.
        # - **NOT**: Matches the tag key but does not match the tag value.
        self.operator = operator
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

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions(DaraModel):
    def __init__(
        self,
        common_file_system_detail: main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail = None,
        common_nas_detail: main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail = None,
        file_detail: main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail = None,
        oss_detail: main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail = None,
        udm_detail: main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail = None,
    ):
        # The advanced options for large-scale file system backup.
        self.common_file_system_detail = common_file_system_detail
        # The advanced options for on-premises NAS.
        self.common_nas_detail = common_nas_detail
        # The advanced options for file backup.
        self.file_detail = file_detail
        # The advanced options for OSS backup.
        self.oss_detail = oss_detail
        # The advanced options for ECS instance backup.
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
            temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m.get('CommonFileSystemDetail'))

        if m.get('CommonNasDetail') is not None:
            temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail()
            self.common_nas_detail = temp_model.from_map(m.get('CommonNasDetail'))

        if m.get('FileDetail') is not None:
            temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail()
            self.file_detail = temp_model.from_map(m.get('FileDetail'))

        if m.get('OssDetail') is not None:
            temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m.get('OssDetail'))

        if m.get('UdmDetail') is not None:
            temp_model = main_models.DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m.get('UdmDetail'))

        return self

class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail(DaraModel):
    def __init__(
        self,
        app_consistent: bool = None,
        destination_kms_key_id: str = None,
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
        # Specifies whether to create an application-consistent snapshot. Creating an application-consistent snapshot is supported only when all cloud disk types are ESSD.
        self.app_consistent = app_consistent
        # The custom KMS key ID in the destination region. If this field is not empty and cross-region replication is enabled, this key is used to encrypt the cross-region replication.
        self.destination_kms_key_id = destination_kms_key_id
        # The list of cloud disk IDs that need to be protected. This value is empty when all cloud disks are protected.
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
        # This parameter is required only when **AppConsistent** is set to **true**. The path of the post-thaw script to execute after creating an application-consistent snapshot.
        self.post_script_path = post_script_path
        # This parameter is required only when **AppConsistent** is set to **true**. The path of the pre-freeze script to execute before creating an application-consistent snapshot.
        self.pre_script_path = pre_script_path
        # This parameter is required only when **AppConsistent** is set to **true**. The RAM role name required for creating application-consistent snapshots.
        self.ram_role_name = ram_role_name
        # Specifies whether to create a snapshot-consistent group. Creating a snapshot-consistent group is supported only when all cloud disk types are ESSD.
        self.snapshot_group = snapshot_group
        # This parameter is required only when **AppConsistent** is set to **true**. The I/O freeze timeout period. Unit: seconds. Default value: 30.
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

        if self.destination_kms_key_id is not None:
            result['DestinationKmsKeyId'] = self.destination_kms_key_id

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

        if m.get('DestinationKmsKeyId') is not None:
            self.destination_kms_key_id = m.get('DestinationKmsKeyId')

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

class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail(DaraModel):
    def __init__(
        self,
        ignore_archive_object: bool = None,
        inventory_cleanup_policy: str = None,
        inventory_id: str = None,
    ):
        # Specifies whether to exclude archive objects from task statistics and failed file lists.
        self.ignore_archive_object = ignore_archive_object
        # Specifies whether to delete inventory files after backup. This parameter is valid only when OSS inventory is used. Valid values:
        # - **NO_CLEANUP**: Do not delete.
        # - **DELETE_CURRENT**: Delete the current file.
        # - **DELETE_CURRENT_AND_PREVIOUS**: Delete all files.
        self.inventory_cleanup_policy = inventory_cleanup_policy
        # The OSS inventory name. If this value is not empty, the OSS inventory is used for performance tuning.
        # - Using an inventory to improve incremental performance is recommended when backing up more than 100 million OSS objects. Storage fees generated by inventory files are charged separately by OSS.
        # - OSS inventory files take time to generate. Backup may fail before the OSS inventory file is generated. Wait for the next cycle to execute.
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

class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail(DaraModel):
    def __init__(
        self,
        adv_policy: bool = None,
        use_vss: bool = None,
    ):
        # Specifies whether to use an advanced policy. Valid values:
        # - **true**: Used.
        # - **false**: Not used.
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

class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        cluster_id: str = None,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The backup client ID.
        self.client_id = client_id
        # The client group ID.
        self.cluster_id = cluster_id
        # The sub-task slice size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether to switch to a full backup when an incremental backup fails. Valid values:
        # - **true**: Switches to a full backup upon failure.
        # - **false**: Does not switch to a full backup upon failure.
        self.full_on_increment_fail = full_on_increment_fail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size

        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')

        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')

        return self

class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail(DaraModel):
    def __init__(
        self,
        fetch_slice_size: int = None,
        full_on_increment_fail: bool = None,
    ):
        # The sub-task slice size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Specifies whether to switch to a full backup when an incremental backup fails. Valid values:
        # - **true**: Switches to a full backup upon failure.
        # - **false**: Does not switch to a full backup upon failure.
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

