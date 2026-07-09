# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEvaluatorResponseBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
        version: str = None,
    ):
        # The evaluator name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The version number that is created.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

