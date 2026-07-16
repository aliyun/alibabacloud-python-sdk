# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPartitionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        partition_name_pattern: str = None,
    ):
        # The maximum number of records to return in a single request.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of results. If the response does not include this token, pass an empty string ("").
        self.page_token = page_token
        # The partition name pattern.
        self.partition_name_pattern = partition_name_pattern

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

        if self.partition_name_pattern is not None:
            result['partitionNamePattern'] = self.partition_name_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('partitionNamePattern') is not None:
            self.partition_name_pattern = m.get('partitionNamePattern')

        return self

