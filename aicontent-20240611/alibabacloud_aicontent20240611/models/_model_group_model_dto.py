# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelGroupModelDTO(DaraModel):
    def __init__(
        self,
        id: int = None,
        model_code: str = None,
        model_type: str = None,
        name: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.id = id
        self.model_code = model_code
        self.model_type = model_type
        self.name = name
        self.platform = platform
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.name is not None:
            result['name'] = self.name

        if self.platform is not None:
            result['platform'] = self.platform

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

