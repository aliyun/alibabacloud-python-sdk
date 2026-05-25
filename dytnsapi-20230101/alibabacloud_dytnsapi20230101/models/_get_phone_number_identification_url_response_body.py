# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20230101 import models as main_models
from darabonba.model import DaraModel

class GetPhoneNumberIdentificationUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPhoneNumberIdentificationUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The return code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **IdentificationNotAvailable**: The verification system does not support the phone number that corresponds to the IP address.
        # *   **MobileNumberIllegal**: The format of the phone number is invalid.
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
            temp_model = main_models.GetPhoneNumberIdentificationUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPhoneNumberIdentificationUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        identification_url: str = None,
        session_id: str = None,
    ):
        # The verification URL.
        self.identification_url = identification_url
        # The session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identification_url is not None:
            result['IdentificationUrl'] = self.identification_url

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentificationUrl') is not None:
            self.identification_url = m.get('IdentificationUrl')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

