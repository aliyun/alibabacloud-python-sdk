# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchTableKnowledgeRequest(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        model: str = None,
        query: str = None,
    ):
        # This parameter is required.
        self.db_id = db_id
        self.model = model
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.model is not None:
            result['Model'] = self.model

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

