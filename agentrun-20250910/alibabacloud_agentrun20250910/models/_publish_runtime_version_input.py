# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishRuntimeVersionInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        publisher: str = None,
    ):
        # 此版本的描述
        self.description = description
        # 发布此版本的用户或系统标识
        self.publisher = publisher

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.publisher is not None:
            result['publisher'] = self.publisher

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')

        return self

