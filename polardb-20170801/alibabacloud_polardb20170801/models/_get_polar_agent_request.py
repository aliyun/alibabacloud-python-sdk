# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPolarAgentRequest(DaraModel):
    def __init__(
        self,
        extra_info: str = None,
        query: str = None,
        session_id: str = None,
        source: str = None,
    ):
        self.extra_info = extra_info
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.query is not None:
            result['Query'] = self.query

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

