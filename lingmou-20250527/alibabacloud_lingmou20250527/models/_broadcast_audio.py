# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BroadcastAudio(DaraModel):
    def __init__(
        self,
        audio_length: int = None,
        create_time: str = None,
        error_code: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
    ):
        self.audio_length = audio_length
        self.create_time = create_time
        self.error_code = error_code
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_length is not None:
            result['audioLength'] = self.audio_length

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.id is not None:
            result['id'] = self.id

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioLength') is not None:
            self.audio_length = m.get('audioLength')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

