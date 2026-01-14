# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetNacosHistoryConfigResponseBody(DaraModel):
    def __init__(
        self,
        configuration: main_models.GetNacosHistoryConfigResponseBodyConfiguration = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The configuration information.
        self.configuration = configuration
        # The error code returned if the request failed.
        self.error_code = error_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            temp_model = main_models.GetNacosHistoryConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m.get('Configuration'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNacosHistoryConfigResponseBodyConfiguration(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        content: str = None,
        data_id: str = None,
        encrypted_data_key: str = None,
        group: str = None,
        md_5: str = None,
        op_type: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The content of the configuration.
        self.content = content
        # The ID of the configuration.
        self.data_id = data_id
        # The encryption key.
        self.encrypted_data_key = encrypted_data_key
        # The name of the configuration group.
        self.group = group
        # The MD5 value of the configuration.
        self.md_5 = md_5
        # The configuration type.
        self.op_type = op_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.content is not None:
            result['Content'] = self.content

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key

        if self.group is not None:
            result['Group'] = self.group

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.op_type is not None:
            result['OpType'] = self.op_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        return self

