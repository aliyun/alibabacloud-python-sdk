# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListSavedSearchResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        savedsearch_items: List[main_models.SavedSearch] = None,
        total: int = None,
    ):
        # The number of saved searches returned on the current page.
        self.count = count
        # The saved searches.
        self.savedsearch_items = savedsearch_items
        # The total number of saved searches that meet the query conditions.
        self.total = total

    def validate(self):
        if self.savedsearch_items:
            for v1 in self.savedsearch_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        result['savedsearchItems'] = []
        if self.savedsearch_items is not None:
            for k1 in self.savedsearch_items:
                result['savedsearchItems'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        self.savedsearch_items = []
        if m.get('savedsearchItems') is not None:
            for k1 in m.get('savedsearchItems'):
                temp_model = main_models.SavedSearch()
                self.savedsearch_items.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

