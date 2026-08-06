# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatabaseDetailsRequest(DaraModel):
    def __init__(
        self,
        database_name_pattern: str = None,
        max_results: int = None,
        page_token: str = None,
        status: str = None,
    ):
        # The SQL-style right fuzzy match pattern for database names. The percent sign (%) wildcard is supported.
        self.database_name_pattern = database_name_pattern
        # The page size.
        # 
        # Default value: 1000.
        # 
        # Maximum value: 1000.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of results. If the response does not include this token, pass an empty string ("") or an empty character (\\"\\").
        self.page_token = page_token
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name_pattern is not None:
            result['databaseNamePattern'] = self.database_name_pattern

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.page_token is not None:
            result['pageToken'] = self.page_token

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseNamePattern') is not None:
            self.database_name_pattern = m.get('databaseNamePattern')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

