# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateModuleResponseBody(DaraModel):
    def __init__(
        self,
        module: str = None,
        properties: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.module = module
        self.properties = properties
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['module'] = self.module

        if self.properties is not None:
            result['properties'] = self.properties

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            self.module = m.get('module')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

