# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListVoiceEnginesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListVoiceEnginesResponseBodyData = None,
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
            temp_model = main_models.ListVoiceEnginesResponseBodyData()
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

class ListVoiceEnginesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        voice_engines: List[main_models.ListVoiceEnginesResponseBodyDataVoiceEngines] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.voice_engines = voice_engines

    def validate(self):
        if self.voice_engines:
            for v1 in self.voice_engines:
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

        result['VoiceEngines'] = []
        if self.voice_engines is not None:
            for k1 in self.voice_engines:
                result['VoiceEngines'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.voice_engines = []
        if m.get('VoiceEngines') is not None:
            for k1 in m.get('VoiceEngines'):
                temp_model = main_models.ListVoiceEnginesResponseBodyDataVoiceEngines()
                self.voice_engines.append(temp_model.from_map(k1))

        return self

class ListVoiceEnginesResponseBodyDataVoiceEngines(DaraModel):
    def __init__(
        self,
        config_schema: str = None,
        nls_engine: str = None,
        nls_engine_name: str = None,
    ):
        self.config_schema = config_schema
        self.nls_engine = nls_engine
        self.nls_engine_name = nls_engine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_schema is not None:
            result['ConfigSchema'] = self.config_schema

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.nls_engine_name is not None:
            result['NlsEngineName'] = self.nls_engine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSchema') is not None:
            self.config_schema = m.get('ConfigSchema')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('NlsEngineName') is not None:
            self.nls_engine_name = m.get('NlsEngineName')

        return self

