# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCheckScopeConfigRequest(DaraModel):
    def __init__(
        self,
        auto_config: str = None,
        auto_type: int = None,
        config_id: str = None,
        resource_directory_account_id: int = None,
        type: int = None,
    ):
        # The JSON string of the automatic scan configuration. The following fields are included:
        # 
        # - **autoInclude**: specifies whether to enable automatic scanning. Valid values: **true**: enabled. **false**: disabled.
        # - **autoRule**: the configuration for enabling automatic scanning.
        # - **ruleOperator**: the rule operator for the configuration. Set the value to **include**.
        # - **operator**: the logical operator. Set the value to **or**.
        # - **rule**: the rule.
        # - **condition**: the rule condition. Valid values: **vendor**: vendor, **assetType**: primary asset type, **assetSubType**: secondary asset type.
        # > For specific meanings, refer to the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation.
        # 
        # This parameter is required when AutoType is set to 1 (automatic scan enabled). Provide a valid JSON configuration string. This parameter is not required when AutoType is set to 0.
        self.auto_config = auto_config
        # The type of the automatic scan configuration. Valid values:
        # - **0**: Automatic scan is disabled.
        # - **1**: Automatically scan newly added cloud assets.
        self.auto_type = auto_type
        # The ID of the configuration.
        # >Call the [GetCheckScopeConfig](~~GetCheckScopeConfig~~) operation to obtain this parameter.
        self.config_id = config_id
        # The ID of the Alibaba Cloud account that corresponds to the member accounts in the resource folder.
        # >Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The type of the scan scope configuration. Valid values:
        # - **1**: scan by instance
        # - **3**: scan all
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config

        if self.auto_type is not None:
            result['AutoType'] = self.auto_type

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')

        if m.get('AutoType') is not None:
            self.auto_type = m.get('AutoType')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

