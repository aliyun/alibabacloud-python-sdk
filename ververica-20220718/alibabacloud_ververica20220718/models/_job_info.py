# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class JobInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
        properties: Dict[str, Any] = None,
    ):
        self.id = id
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.properties is not None:
            result['properties'] = self.properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        return self

