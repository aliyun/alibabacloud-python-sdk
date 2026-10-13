# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaCompareIncrementDbOverviewRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        is_summary: bool = None,
        task_id: int = None,
    ):
        # The name of the catalog. In a multi-catalog environment, it is used to locate the catalog where the destination database resides.
        self.catalog_name = catalog_name
        # The name of the database for which you want to query incremental changes.
        # 
        # This parameter is required.
        self.db_name = db_name
        # Specifies whether to return only summary statistics.
        self.is_summary = is_summary
        # The ID of the metadata comparison task, which is obtained from the return value of the create or save comparison task API operation.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.is_summary is not None:
            result['isSummary'] = self.is_summary

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('isSummary') is not None:
            self.is_summary = m.get('isSummary')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

