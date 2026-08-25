# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServerIdeImagesRequest(DaraModel):
    def __init__(
        self,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The image label filter condition. Separate multiple Key=Value conditions with commas.
        self.labels = labels
        # The maximum number of records to return in a single request.
        self.max_results = max_results
        # The image name filter condition. Supports fuzzy match.
        self.name = name
        # The pagination token used to continue a query. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The page number. The value starts from 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

