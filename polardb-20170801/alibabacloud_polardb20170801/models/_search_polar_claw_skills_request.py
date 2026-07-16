# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchPolarClawSkillsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        limit: int = None,
        query: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The maximum number of results to return. Valid values: 1 to 100.
        self.limit = limit
        # The search keyword. If this parameter is not specified, popular or recommended results are returned.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

