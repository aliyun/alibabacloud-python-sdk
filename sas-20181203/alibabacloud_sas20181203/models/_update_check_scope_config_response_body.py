# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateCheckScopeConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateCheckScopeConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The returned data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateCheckScopeConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateCheckScopeConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_config: str = None,
        auto_type: int = None,
        config_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        type: int = None,
    ):
        # The automatic scan configuration as a JSON string. The following fields are included:
        # 
        # - **autoInclude**: specifies whether to enable automatic scan. Valid values: **true**: enabled. **false**: disabled.
        # - **autoRule**: the enablement configuration.
        # - **ruleOperator**: the enablement configuration rule. Set the value to **include**.
        # - **operator**: the logical operator. Set the value to **or**.
        # - **rule**: the rule.
        # - **condition**: the rule condition. Valid values: **vendor**: vendor. **assetType**: level-1 asset type. **assetSubType**: level-2 asset type.
        # > For more information, refer to the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation.
        self.auto_config = auto_config
        # The automatic scan configuration type. Valid values:
        # - **0**: disable automatic scan
        # - **1**: automatically scan newly added cloud assets
        self.auto_type = auto_type
        # The ID of the configuration.
        self.config_id = config_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The scan scope configuration type. Valid values:
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

