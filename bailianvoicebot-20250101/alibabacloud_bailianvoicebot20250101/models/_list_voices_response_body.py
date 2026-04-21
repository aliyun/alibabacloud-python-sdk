# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class ListVoicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListVoicesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListVoicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVoicesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        voices: List[main_models.ListVoicesResponseBodyDataVoices] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.voices = voices

    def validate(self):
        if self.voices:
            for v1 in self.voices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Voices'] = []
        if self.voices is not None:
            for k1 in self.voices:
                result['Voices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.voices = []
        if m.get('Voices') is not None:
            for k1 in m.get('Voices'):
                temp_model = main_models.ListVoicesResponseBodyDataVoices()
                self.voices.append(temp_model.from_map(k1))

        return self

class ListVoicesResponseBodyDataVoices(DaraModel):
    def __init__(
        self,
        category: str = None,
        language: str = None,
        model: str = None,
        name: str = None,
        nls_engine: str = None,
        style: str = None,
        supported_params: List[str] = None,
        voice: str = None,
    ):
        self.category = category
        self.language = language
        self.model = model
        self.name = name
        self.nls_engine = nls_engine
        self.style = style
        self.supported_params = supported_params
        self.voice = voice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.language is not None:
            result['Language'] = self.language

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.style is not None:
            result['Style'] = self.style

        if self.supported_params is not None:
            result['SupportedParams'] = self.supported_params

        if self.voice is not None:
            result['Voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('SupportedParams') is not None:
            self.supported_params = m.get('SupportedParams')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self

