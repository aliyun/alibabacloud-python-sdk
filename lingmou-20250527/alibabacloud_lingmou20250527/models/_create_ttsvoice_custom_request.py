# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTTSVoiceCustomRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        gender: str = None,
        name: str = None,
        oss_key: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        self.gender = gender
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.name is not None:
            result['name'] = self.name

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        return self

