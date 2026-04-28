# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class SearchShareLinkResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ShareLink] = None,
        next_marker: str = None,
        total_count: int = None,
    ):
        # The share URLs.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.next_marker is not None:
            result['next_marker'] = self.next_marker

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ShareLink()
                self.items.append(temp_model.from_map(k1))

        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

