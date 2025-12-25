# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnalyzeSQLLineageRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        sql_content: str = None,
        tid: int = None,
    ):
        # The database ID.
        # 
        # >  You can call one of the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html), [ListDatabases](https://help.aliyun.com/document_detail/141873.html), and [GetDatabase](https://help.aliyun.com/document_detail/141869.html) operations to obtain the database ID provided in the DatabaseId response parameter.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The SQL statement.
        # 
        # This parameter is required.
        self.sql_content = sql_content
        # The tenant ID.
        # 
        # >  To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.sql_content is not None:
            result['SqlContent'] = self.sql_content

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('SqlContent') is not None:
            self.sql_content = m.get('SqlContent')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

