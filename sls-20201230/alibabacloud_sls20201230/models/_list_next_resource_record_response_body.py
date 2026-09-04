# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListNextResourceRecordResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ResourceRecord] = None,
        max_results: int = None,
        next_token: str = None,
        total: int = None,
    ):
        # The list of resource records.
        self.items = items
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more data is available.
        self.next_token = next_token
        # The total number of records that match the filter criteria.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ResourceRecord()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

