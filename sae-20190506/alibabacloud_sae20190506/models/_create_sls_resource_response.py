# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSlsResourceResponse(DaraModel):
    def __init__(
        self,
        log_store: str = None,
        project: str = None,
        request_id: str = None,
    ):
        self.log_store = log_store
        self.project = project
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store is not None:
            result['logStore'] = self.log_store

        if self.project is not None:
            result['project'] = self.project

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logStore') is not None:
            self.log_store = m.get('logStore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

