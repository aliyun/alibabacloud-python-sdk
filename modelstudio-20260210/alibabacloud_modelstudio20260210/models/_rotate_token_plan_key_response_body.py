# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class RotateTokenPlanKeyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RotateTokenPlanKeyResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The business data.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.RotateTokenPlanKeyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RotateTokenPlanKeyResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key_id: str = None,
        masked_api_key: str = None,
        plain_api_key: str = None,
        reset_at: str = None,
        source_id: str = None,
    ):
        # The API Key ID, which is system-generated.
        self.api_key_id = api_key_id
        # The new masked_api_key returned by BaiLian, such as sk_***cdef.
        self.masked_api_key = masked_api_key
        # The new plaintext API Key returned by BaiLian. This value is returned only once during the reset operation.
        self.plain_api_key = plain_api_key
        # The time when the API key was reset.
        self.reset_at = reset_at
        # The source_id returned by BaiLian.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.masked_api_key is not None:
            result['MaskedApiKey'] = self.masked_api_key

        if self.plain_api_key is not None:
            result['PlainApiKey'] = self.plain_api_key

        if self.reset_at is not None:
            result['ResetAt'] = self.reset_at

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('MaskedApiKey') is not None:
            self.masked_api_key = m.get('MaskedApiKey')

        if m.get('PlainApiKey') is not None:
            self.plain_api_key = m.get('PlainApiKey')

        if m.get('ResetAt') is not None:
            self.reset_at = m.get('ResetAt')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

