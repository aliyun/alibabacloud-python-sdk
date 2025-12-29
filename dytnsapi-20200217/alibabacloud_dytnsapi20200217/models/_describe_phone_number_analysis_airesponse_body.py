# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneNumberAnalysisAIResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.DescribePhoneNumberAnalysisAIResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code. Valid values:
        # 
        # *   OK: The request is successful.
        self.code = code
        # The response parameters.
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribePhoneNumberAnalysisAIResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneNumberAnalysisAIResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        number: str = None,
    ):
        # The returned code.
        # 
        # *   YES: The specified phone number is valid.
        # *   NO: The specified phone number is invalid.
        # *   UNKNOWN: The specified phone number is unknown
        self.code = code
        # The specified phone number.
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.number is not None:
            result['Number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        return self

