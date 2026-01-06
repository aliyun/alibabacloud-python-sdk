# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class OpenStructMVRecommendResultModel(DaraModel):
    def __init__(
        self,
        accelerated_queries_count: int = None,
        base_tables: List[main_models.OpenStructMvBaseTableDetailModel] = None,
        saved_scanbytes: int = None,
        subquery: str = None,
        subquery_id: int = None,
        support_incremental_refresh: bool = None,
    ):
        self.accelerated_queries_count = accelerated_queries_count
        self.base_tables = base_tables
        self.saved_scanbytes = saved_scanbytes
        self.subquery = subquery
        self.subquery_id = subquery_id
        self.support_incremental_refresh = support_incremental_refresh

    def validate(self):
        if self.base_tables:
            for v1 in self.base_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerated_queries_count is not None:
            result['AcceleratedQueriesCount'] = self.accelerated_queries_count

        result['BaseTables'] = []
        if self.base_tables is not None:
            for k1 in self.base_tables:
                result['BaseTables'].append(k1.to_map() if k1 else None)

        if self.saved_scanbytes is not None:
            result['SavedScanbytes'] = self.saved_scanbytes

        if self.subquery is not None:
            result['Subquery'] = self.subquery

        if self.subquery_id is not None:
            result['SubqueryId'] = self.subquery_id

        if self.support_incremental_refresh is not None:
            result['SupportIncrementalRefresh'] = self.support_incremental_refresh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratedQueriesCount') is not None:
            self.accelerated_queries_count = m.get('AcceleratedQueriesCount')

        self.base_tables = []
        if m.get('BaseTables') is not None:
            for k1 in m.get('BaseTables'):
                temp_model = main_models.OpenStructMvBaseTableDetailModel()
                self.base_tables.append(temp_model.from_map(k1))

        if m.get('SavedScanbytes') is not None:
            self.saved_scanbytes = m.get('SavedScanbytes')

        if m.get('Subquery') is not None:
            self.subquery = m.get('Subquery')

        if m.get('SubqueryId') is not None:
            self.subquery_id = m.get('SubqueryId')

        if m.get('SupportIncrementalRefresh') is not None:
            self.support_incremental_refresh = m.get('SupportIncrementalRefresh')

        return self

