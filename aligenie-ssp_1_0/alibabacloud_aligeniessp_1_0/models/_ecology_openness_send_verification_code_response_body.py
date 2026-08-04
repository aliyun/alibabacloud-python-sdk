# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class EcologyOpennessSendVerificationCodeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.EcologyOpennessSendVerificationCodeResponseBodyResult = None,
        success: bool = None,
    ):
        # Response code
        self.code = code
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Response Result
        self.result = result
        # Flag indicating whether the invocation succeeded
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.EcologyOpennessSendVerificationCodeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EcologyOpennessSendVerificationCodeResponseBodyResult(DaraModel):
    def __init__(
        self,
        expire_in: int = None,
        repeat_interval: int = None,
    ):
        # Validity Period (unit: seconds)
        self.expire_in = expire_in
        # Recency before the next resend is allowed (unit: seconds)
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_in is not None:
            result['ExpireIn'] = self.expire_in

        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireIn') is not None:
            self.expire_in = m.get('ExpireIn')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        return self

