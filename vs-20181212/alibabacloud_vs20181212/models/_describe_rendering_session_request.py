# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRenderingSessionRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        project_id: str = None,
        session_id: str = None,
    ):
        self.client_id = client_id
        # This parameter is required.
        self.project_id = project_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

