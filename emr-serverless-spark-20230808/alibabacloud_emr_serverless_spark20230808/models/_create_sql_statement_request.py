# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSqlStatementRequest(DaraModel):
    def __init__(
        self,
        code_content: str = None,
        default_catalog: str = None,
        default_database: str = None,
        limit: int = None,
        sql_compute_id: str = None,
        task_biz_id: str = None,
        region_id: str = None,
    ):
        # The SQL code. You can specify one or more SQL statements.
        self.code_content = code_content
        # The default Data Lake Formation (DLF) catalog ID.
        self.default_catalog = default_catalog
        # The name of the default database.
        self.default_database = default_database
        # The maximum number of entries to return. Valid values: 1 to 10000.
        self.limit = limit
        # The SQL session ID. You can create an SQL session in the workspace created in EMR Serverless Spark.
        self.sql_compute_id = sql_compute_id
        self.task_biz_id = task_biz_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_content is not None:
            result['codeContent'] = self.code_content

        if self.default_catalog is not None:
            result['defaultCatalog'] = self.default_catalog

        if self.default_database is not None:
            result['defaultDatabase'] = self.default_database

        if self.limit is not None:
            result['limit'] = self.limit

        if self.sql_compute_id is not None:
            result['sqlComputeId'] = self.sql_compute_id

        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeContent') is not None:
            self.code_content = m.get('codeContent')

        if m.get('defaultCatalog') is not None:
            self.default_catalog = m.get('defaultCatalog')

        if m.get('defaultDatabase') is not None:
            self.default_database = m.get('defaultDatabase')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('sqlComputeId') is not None:
            self.sql_compute_id = m.get('sqlComputeId')

        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

