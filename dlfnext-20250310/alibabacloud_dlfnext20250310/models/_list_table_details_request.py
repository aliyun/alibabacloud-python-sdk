# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTableDetailsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        status: str = None,
        table_name_pattern: str = None,
        type: str = None,
    ):
        # The maximum number of records to retrieve in a single request.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of data. If the response does not provide this value, pass an empty string ("") or an empty character (\\"\\").
        self.page_token = page_token
        # The deletion status of the table. Valid values:
        # - retained: The table is deleted and temporarily stored in the recycle bin.
        # - active: The table is in a normal state. This is the default value.
        self.status = status
        # The fuzzy match pattern for the table name.
        self.table_name_pattern = table_name_pattern
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.page_token is not None:
            result['pageToken'] = self.page_token

        if self.status is not None:
            result['status'] = self.status

        if self.table_name_pattern is not None:
            result['tableNamePattern'] = self.table_name_pattern

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tableNamePattern') is not None:
            self.table_name_pattern = m.get('tableNamePattern')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

