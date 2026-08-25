# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolicyBindingShrinkRequest(DaraModel):
    def __init__(
        self,
        advanced_options_shrink: str = None,
        data_source_id: str = None,
        disabled: bool = None,
        exclude: str = None,
        include: str = None,
        policy_binding_description: str = None,
        policy_id: str = None,
        source: str = None,
        source_type: str = None,
        speed_limit: str = None,
    ):
        # The advanced options.
        self.advanced_options_shrink = advanced_options_shrink
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Specifies whether the policy is suspended for the data source.
        # - true: Suspended.
        # - false: Not suspended.
        self.disabled = disabled
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**, **File**, **NAS**, **COMMON_NAS**, or **COMMON_FILE_SYSTEM**. Specifies the file types to back up. All files of these types are backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**, **File**, **NAS**, **COMMON_NAS**, or **COMMON_FILE_SYSTEM**. Specifies the file types to back up. All files of these types are backed up. The value can be up to 255 characters in length.
        self.include = include
        # The description of the policy binding.
        self.policy_binding_description = policy_binding_description
        # The policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The meaning varies depending on the SourceType value:
        # - **OSS**: The prefix to back up. If not specified, the entire root directory of the bucket is backed up. Only a single prefix is supported. To back up /backup, set this parameter to /backup.
        # - **ECS_FILE**: The file directories to back up. If not specified, all directories are backed up. Multiple directories are supported. To back up files in /a and /b, set this parameter to ["/a", "/b"].
        # - **File**: The file directories to back up. If not specified, all directories are backed up. Multiple directories are supported. To back up files in /a and /b, set this parameter to ["/a", "/b"].
        # - **COMMON_FILE_SYSTEM**: Required. The source paths to back up. Multiple paths are supported. To back up /a and /b, set this parameter to ["/a", "/b"]. To back up the root path, set this parameter to ["/"].
        # - **COMMON_NAS**: Required. The source path to back up. Only a single path is supported. To back up /a, set this parameter to ["/a"]. To back up the root path, set this parameter to ["/"].
        # - **OTS**: The list of data tables to back up. If not specified, all data tables are backed up. Multiple data tables are supported. To back up data tables a and b, set this parameter to ["a", "b"].
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
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required only when **SourceType** is set to **ECS_FILE** or **File**. Specifies the backup traffic control. The format is `{start}{end}{bandwidth}`. Multiple traffic control configurations are separated by delimiters, and the time ranges cannot overlap.
        # 
        # - **start**: The start hour.
        # - **end**: The end hour.
        # - **bandwidth**: The rate limit, in KB/s.
        self.speed_limit = speed_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_options_shrink is not None:
            result['AdvancedOptions'] = self.advanced_options_shrink

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

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

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
            self.advanced_options_shrink = m.get('AdvancedOptions')

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

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        return self

