# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class UpgradeToRCSSignatureResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.UpgradeToRCSSignatureResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.UpgradeToRCSSignatureResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpgradeToRCSSignatureResponseBodyData(DaraModel):
    def __init__(
        self,
        chatbot_code: str = None,
        sign_id: int = None,
    ):
        self.chatbot_code = chatbot_code
        self.sign_id = sign_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chatbot_code is not None:
            result['ChatbotCode'] = self.chatbot_code

        if self.sign_id is not None:
            result['SignId'] = self.sign_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatbotCode') is not None:
            self.chatbot_code = m.get('ChatbotCode')

        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')

        return self

