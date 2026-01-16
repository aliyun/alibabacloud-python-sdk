# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ListSessionsOutput(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        sessions: List[main_models.Session] = None,
    ):
        self.next_token = next_token
        self.sessions = sessions

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
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['sessions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.sessions = []
        if m.get('sessions') is not None:
            for k1 in m.get('sessions'):
                temp_model = main_models.Session()
                self.sessions.append(temp_model.from_map(k1))

        return self

