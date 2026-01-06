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
        # The ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Specifies whether to disable the backup policy for the data source. Valid values:
        # 
        # *   true: disables the backup policy for the data source
        # *   false: enables the backup policy for the data source
        self.disabled = disabled
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the type of files that do not need to be backed up. No files of the specified type are backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the type of files to be backed up. All files of the specified type are backed up. The value can be up to 255 characters in length.
        self.include = include
        # The description of the association.
        self.policy_binding_description = policy_binding_description
        # The ID of the backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # *   If the SourceType parameter is set to **OSS**, set the Source parameter to the prefix of the path to the folder that you want to back up. If you do not specify the Source parameter, the entire bucket (root directory) is backed up.
        # *   If the SourceType parameter is set to **ECS_FILE** or **File**, set the Source parameter to the path to the files that you want to back up. If you do not specify the Source parameter, all paths backed up.
        self.source = source
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE** or **File**. This parameter specifies the throttling rules. Format: `{start}{end}{bandwidth}`. Separate multiple throttling rules with vertical bars (|). The time ranges of the throttling rules cannot overlap.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
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

