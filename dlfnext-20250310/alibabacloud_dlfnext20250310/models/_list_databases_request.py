# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class ListDatabasesRequest(DaraModel):
    def __init__(
        self,
        database_name_pattern: str = None,
        max_results: int = None,
        page_token: str = None,
    ):
        self.database_name_pattern = database_name_pattern
        self.max_results = max_results
        self.page_token = page_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseNamePattern') is not None:
            self.database_name_pattern = m.get('databaseNamePattern')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        return self

