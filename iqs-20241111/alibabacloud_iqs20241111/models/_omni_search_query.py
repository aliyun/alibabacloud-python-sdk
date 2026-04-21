# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OmniSearchQuery(DaraModel):
    def __init__(
        self,
        query: str = None,
        session_id: str = None,
        use_cot: bool = None,
        use_model: str = None,
    ):
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.use_cot = use_cot
        self.use_model = use_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['query'] = self.query

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.use_cot is not None:
            result['useCot'] = self.use_cot

        if self.use_model is not None:
            result['useModel'] = self.use_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('useCot') is not None:
            self.use_cot = m.get('useCot')

        if m.get('useModel') is not None:
            self.use_model = m.get('useModel')

        return self

