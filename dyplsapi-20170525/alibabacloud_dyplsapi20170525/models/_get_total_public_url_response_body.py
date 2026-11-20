# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetTotalPublicUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTotalPublicUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The download URLs of the recording files.
        self.data = data
        # The returned message.
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
            temp_model = main_models.GetTotalPublicUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTotalPublicUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        phone_public_url: str = None,
        ring_public_url: str = None,
    ):
        # The download URL of the recorded call.
        # 
        # >  The download URL of the recorded call is valid for 30 days.
        self.phone_public_url = phone_public_url
        # The download URL of the recorded ringing tone.
        # 
        # >  The download URL of the recorded ringing tone is valid for 30 days.
        self.ring_public_url = ring_public_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_public_url is not None:
            result['PhonePublicUrl'] = self.phone_public_url

        if self.ring_public_url is not None:
            result['RingPublicUrl'] = self.ring_public_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhonePublicUrl') is not None:
            self.phone_public_url = m.get('PhonePublicUrl')

        if m.get('RingPublicUrl') is not None:
            self.ring_public_url = m.get('RingPublicUrl')

        return self

