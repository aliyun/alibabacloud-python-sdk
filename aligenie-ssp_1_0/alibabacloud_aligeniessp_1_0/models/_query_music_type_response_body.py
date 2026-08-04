# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryMusicTypeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.QueryMusicTypeResponseBodyResult] = None,
    ):
        # Status code returned by the alarm service
        self.code = code
        # error message
        self.message = message
        # request ID
        self.request_id = request_id
        # List of ringtone types
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

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

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryMusicTypeResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class QueryMusicTypeResponseBodyResult(DaraModel):
    def __init__(
        self,
        music_type: int = None,
        music_type_name: str = None,
    ):
        # Ringtone type ID
        self.music_type = music_type
        # Name of the ringtone category
        self.music_type_name = music_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.music_type is not None:
            result['MusicType'] = self.music_type

        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')

        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')

        return self

