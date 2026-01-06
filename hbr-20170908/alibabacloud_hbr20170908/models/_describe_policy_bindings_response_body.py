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
        # Return code, 200 indicates success.
        self.code = code
        # The number of results per query.
        # 
        # Range: 10~100. Default: 10.
        self.max_results = max_results
        # Description of the return message. A successful response usually returns \\"successful\\", while an error will return a corresponding error message.
        self.message = message
        # The token required to fetch the next page of policy and data source bindings.
        self.next_token = next_token
        # List of bound policies.
        self.policy_bindings = policy_bindings
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: Success
        # - false: Failure
        self.success = success
        # Total number of records.
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
        # Advanced options.
        self.advanced_options = advanced_options
        # Whether the resource is automatically associated through the backup policy resource tag.
        self.created_by_tag = created_by_tag
        # Creation time. UNIX timestamp, in seconds.
        self.created_time = created_time
        # The name of the role created in the RAM of the original account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values: 
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The ID of the original account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # Data source ID.
        self.data_source_id = data_source_id
        # Whether the policy is disbaled for this data source.
        # - true: disabled
        # - false: Not disabled
        self.disabled = disabled
        # This parameter is required only when **SourceType** is **ECS_FILE** or **File**. It specifies the file types that should not be backed up, and all files of these types will be excluded. Supports up to 255 characters.
        self.exclude = exclude
        # Hit tag rules.
        self.hit_tags = hit_tags
        # This parameter is required only when **SourceType** is **ECS_FILE** or **File**. It specifies the file types to be backed up, and all files of these types will be backed up. Supports up to 255 characters.
        self.include = include
        # Bound policy description.
        self.policy_binding_description = policy_binding_description
        # Bound policy ID.
        self.policy_binding_id = policy_binding_id
        # Policy ID.
        self.policy_id = policy_id
        # - When **SourceType** is **OSS**, it indicates the prefix to be backed up. If not specified, it means backing up the entire root directory of the Bucket.
        # - When **SourceType** is **ECS_FILE** or **File**, it indicates the file directory to be backed up. If not specified, it means backing up all directories.
        self.source = source
        # Data source type, with the value range:
        # - **UDM_ECS**: indicates ECS full machine backup
        self.source_type = source_type
        # This parameter is required only when **SourceType** is **ECS_FILE** or **File**. It specifies the backup traffic control. The format is `{start}{end}{bandwidth}`. Multiple traffic control configurations are separated by commas, and the configured times must not overlap.
        # 
        # - **start**: Start hour.
        # - **end**: End hour.
        # - **bandwidth**: Limit rate, in KB/s.
        self.speed_limit = speed_limit
        # Update time. UNIX timestamp, in seconds.
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
        # Tag key.
        self.key = key
        # Tag matching rule.
        # - **EQUAL**: Matches both the tag key and tag value.
        # - **NOT**: Matches the tag key but not the tag value.
        self.operator = operator
        # Tag value.
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
        # Advanced options for large-scale file system backup.
        self.common_file_system_detail = common_file_system_detail
        # Advanced options for local NAS.
        self.common_nas_detail = common_nas_detail
        # Advanced options for file backup.
        self.file_detail = file_detail
        # Advanced options for OSS backup.
        self.oss_detail = oss_detail
        # Advanced options for full machine backup.
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
        # 是否创建应用一致性。仅云盘类型全部为ESSD时，支持创建快照应用一致性。
        self.app_consistent = app_consistent
        # The custom KMS key ID in the destination region. When this field is not empty and cross-region replication is enabled, the specified key will be used for encrypting the cross-region replication.
        self.destination_kms_key_id = destination_kms_key_id
        # List of disk IDs that need protection. This value is empty when protecting all disks.
        self.disk_id_list = disk_id_list
        # This parameter is required when **AppConsistent** is **true**. It indicates whether to use the Linux FsFreeze mechanism to ensure the file system is in a read-only consistent state before creating an application-consistent snapshot. The default value is true.
        self.enable_fs_freeze = enable_fs_freeze
        # This parameter is required when **AppConsistent** is **true**. It determines whether to set an application-consistent snapshot:
        # - **true**: Create an application-consistent snapshot
        # - **false**: Create a file system-consistent snapshot
        # 
        # The default value is true.
        self.enable_writers = enable_writers
        # List of disk IDs that do not need protection. This parameter is ignored if DiskIdList is not empty.
        self.exclude_disk_id_list = exclude_disk_id_list
        # This parameter is required when **AppConsistent** is **true**. It specifies the path of the unfreeze script to be executed after creating an application-consistent snapshot.
        self.post_script_path = post_script_path
        # This parameter is required when **AppConsistent** is **true**. It specifies the path of the freeze script to be executed before creating an application-consistent snapshot.
        self.pre_script_path = pre_script_path
        # This parameter is required when **AppConsistent** is **true**. It specifies the RAM role name needed for creating an application-consistent snapshot.
        self.ram_role_name = ram_role_name
        # Indicates whether to create a snapshot consistency group. Only supported when all disk types are ESSD.
        self.snapshot_group = snapshot_group
        # This parameter is required when **AppConsistent** is **true**. It specifies the IO freeze timeout duration. The default value is 30 seconds.
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
        # Do not prompt for archive-type objects in the task statistics and failed file list.
        self.ignore_archive_object = ignore_archive_object
        # Whether to delete the inventory file after the backup. This is only effective when using an OSS inventory. Supported values:
        # - **NO_CLEANUP**: Do not delete.
        # - **DELETE_CURRENT**: Delete the current file.
        # - **DELETE_CURRENT_AND_PREVIOUS**: Delete all files.
        self.inventory_cleanup_policy = inventory_cleanup_policy
        # The name of the OSS inventory. If this value is not empty, the OSS inventory will be used for performance optimization.
        # - It is recommended to use an inventory for backing up more than 100 million OSS objects to improve incremental performance. Storage costs for the inventory files are charged separately by the OSS service.
        # - The generation of the OSS inventory file takes time, and the backup may fail before the inventory file is generated. You can wait for the next cycle to execute.
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
        # Whether to use advanced policies. Values:
        # - **true**: Use.
        # - **false**: Do not use.
        self.adv_policy = adv_policy
        # Whether to enable VSS (Windows) functionality. Values:
        # - **true**: Enable.
        # - **false**: Disable.
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
        # Backup client ID.
        self.client_id = client_id
        # Client group ID.
        self.cluster_id = cluster_id
        # Backup slice size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Whether to switch to a full backup when an incremental backup fails. Values:
        # - **true**: Switch to full backup on failure.
        # - **false**: Do not switch to full backup on failure.
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
        # Backup shard size (number of files).
        self.fetch_slice_size = fetch_slice_size
        # Whether to switch to a full backup when an incremental backup fails. Values:
        # - **true**: Switch to full backup on failure.
        # - **false**: Do not switch to full backup on failure.
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

