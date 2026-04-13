# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paicopilot20250731 import models as main_models
from darabonba.model import DaraModel

class ListSessionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sessions: List[main_models.Session] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sessions = sessions
        self.total_count = total_count

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.Session()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

