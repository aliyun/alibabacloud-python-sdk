# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchPolarClawSkillsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        exact: bool = None,
        limit: int = None,
        query: str = None,
        source: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to perform an exact search by matching the slug.
        self.exact = exact
        # The maximum number of results to return. Valid values: 1 to 100.
        self.limit = limit
        # The search keyword. If this parameter is not specified, popular or recommended skills are returned.
        self.query = query
        # The source of the skill. Valid values: clawhub and polarhub.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.exact is not None:
            result['Exact'] = self.exact

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.query is not None:
            result['Query'] = self.query

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Exact') is not None:
            self.exact = m.get('Exact')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

