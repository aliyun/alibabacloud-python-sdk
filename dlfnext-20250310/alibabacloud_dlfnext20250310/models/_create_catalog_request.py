# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateCatalogRequest(DaraModel):
    def __init__(
        self,
        is_shared: bool = None,
        name: str = None,
        options: Dict[str, str] = None,
        share_id: str = None,
        type: str = None,
    ):
        self.is_shared = is_shared
        self.name = name
        self.options = options
        self.share_id = share_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_shared is not None:
            result['isShared'] = self.is_shared

        if self.name is not None:
            result['name'] = self.name

        if self.options is not None:
            result['options'] = self.options

        if self.share_id is not None:
            result['shareId'] = self.share_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isShared') is not None:
            self.is_shared = m.get('isShared')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

