# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class CreateCloneVoiceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCloneVoiceResponseBodyData = None,
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
            temp_model = main_models.CreateCloneVoiceResponseBodyData()
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

class CreateCloneVoiceResponseBodyData(DaraModel):
    def __init__(
        self,
        clone_voice_id: str = None,
        voice: str = None,
    ):
        self.clone_voice_id = clone_voice_id
        self.voice = voice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clone_voice_id is not None:
            result['CloneVoiceId'] = self.clone_voice_id

        if self.voice is not None:
            result['Voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneVoiceId') is not None:
            self.clone_voice_id = m.get('CloneVoiceId')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self

