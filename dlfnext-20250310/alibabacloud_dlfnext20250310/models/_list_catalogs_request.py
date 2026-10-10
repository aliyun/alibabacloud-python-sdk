# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCatalogsRequest(DaraModel):
    def __init__(
        self,
        catalog_name_pattern: str = None,
        max_results: int = None,
        page_token: str = None,
    ):
        # The catalog name pattern.
        self.catalog_name_pattern = catalog_name_pattern
        # The maximum number of records to retrieve at a time.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of results. If the response does not include a token, pass an empty string ("") or an empty character (\\"\\").
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name_pattern is not None:
            result['catalogNamePattern'] = self.catalog_name_pattern

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.page_token is not None:
            result['pageToken'] = self.page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogNamePattern') is not None:
            self.catalog_name_pattern = m.get('catalogNamePattern')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        return self

