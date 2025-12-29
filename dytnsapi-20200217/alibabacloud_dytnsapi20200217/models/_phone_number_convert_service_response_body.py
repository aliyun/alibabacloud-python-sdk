# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class PhoneNumberConvertServiceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.PhoneNumberConvertServiceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.PhoneNumberConvertServiceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PhoneNumberConvertServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        conver_result: bool = None,
        number: str = None,
        number_md_5: str = None,
        number_sha_256: str = None,
    ):
        self.conver_result = conver_result
        self.number = number
        self.number_md_5 = number_md_5
        self.number_sha_256 = number_sha_256

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conver_result is not None:
            result['ConverResult'] = self.conver_result

        if self.number is not None:
            result['Number'] = self.number

        if self.number_md_5 is not None:
            result['NumberMd5'] = self.number_md_5

        if self.number_sha_256 is not None:
            result['NumberSha256'] = self.number_sha_256

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConverResult') is not None:
            self.conver_result = m.get('ConverResult')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('NumberMd5') is not None:
            self.number_md_5 = m.get('NumberMd5')

        if m.get('NumberSha256') is not None:
            self.number_sha_256 = m.get('NumberSha256')

        return self

