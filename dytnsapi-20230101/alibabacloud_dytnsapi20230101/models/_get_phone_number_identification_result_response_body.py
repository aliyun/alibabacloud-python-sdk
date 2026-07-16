# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20230101 import models as main_models
from darabonba.model import DaraModel

class GetPhoneNumberIdentificationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPhoneNumberIdentificationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The return code. Valid values:
        # 
        # *   OK: The request is successful.
        # *   NoIdentificationResult: No verification result is available or the verification failed.
        # *   SessionNotValid: The session is invalid or expired.
        # *   MobileNumberIllegal: The format of the phone number is invalid.
        self.code = code
        # The returned data.
        self.data = data
        # The description of the return code.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetPhoneNumberIdentificationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPhoneNumberIdentificationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        is_identified: str = None,
    ):
        # Indicates whether the phone number passed the verification.
        self.is_identified = is_identified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_identified is not None:
            result['IsIdentified'] = self.is_identified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsIdentified') is not None:
            self.is_identified = m.get('IsIdentified')

        return self

