# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInstanceDatasourceRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

