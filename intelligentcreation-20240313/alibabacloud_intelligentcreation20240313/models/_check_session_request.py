# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckSessionRequest(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        session_id: str = None,
    ):
        self.project_id = project_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

