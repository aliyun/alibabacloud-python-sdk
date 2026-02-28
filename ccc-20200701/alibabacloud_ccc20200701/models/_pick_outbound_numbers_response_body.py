# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class PickOutboundNumbersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.PickOutboundNumbersResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
                temp_model = main_models.PickOutboundNumbersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PickOutboundNumbersResponseBodyData(DaraModel):
    def __init__(
        self,
        callee: main_models.PickOutboundNumbersResponseBodyDataCallee = None,
        caller: main_models.PickOutboundNumbersResponseBodyDataCaller = None,
    ):
        self.callee = callee
        self.caller = caller

    def validate(self):
        if self.callee:
            self.callee.validate()
        if self.caller:
            self.caller.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee is not None:
            result['Callee'] = self.callee.to_map()

        if self.caller is not None:
            result['Caller'] = self.caller.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            temp_model = main_models.PickOutboundNumbersResponseBodyDataCallee()
            self.callee = temp_model.from_map(m.get('Callee'))

        if m.get('Caller') is not None:
            temp_model = main_models.PickOutboundNumbersResponseBodyDataCaller()
            self.caller = temp_model.from_map(m.get('Caller'))

        return self

class PickOutboundNumbersResponseBodyDataCaller(DaraModel):
    def __init__(
        self,
        city: str = None,
        number: str = None,
        province: str = None,
    ):
        self.city = city
        self.number = number
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.number is not None:
            result['Number'] = self.number

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

class PickOutboundNumbersResponseBodyDataCallee(DaraModel):
    def __init__(
        self,
        city: str = None,
        number: str = None,
        province: str = None,
    ):
        self.city = city
        self.number = number
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.number is not None:
            result['Number'] = self.number

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

