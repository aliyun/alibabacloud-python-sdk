# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreateSmsSignResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CreateSmsSignResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned status code. Valid values:
        # 
        # - 0000: The request is successful.
        # 
        # - Other values: The request failed.
        self.code = code
        # The text message signature creation result.
        self.data = data
        # The returned message.
        self.message = message
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateSmsSignResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSmsSignResponseBodyData(DaraModel):
    def __init__(
        self,
        called_no_sign: str = None,
    ):
        # The signature string of the recipient number. Append this string to the text message content to parse the actual called number.
        self.called_no_sign = called_no_sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_no_sign is not None:
            result['CalledNoSign'] = self.called_no_sign

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNoSign') is not None:
            self.called_no_sign = m.get('CalledNoSign')

        return self

