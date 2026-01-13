# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListSqlStatementContentsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sql_statement_contents: main_models.ListSqlStatementContentsResponseBodySqlStatementContents = None,
    ):
        self.request_id = request_id
        self.sql_statement_contents = sql_statement_contents

    def validate(self):
        if self.sql_statement_contents:
            self.sql_statement_contents.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sql_statement_contents is not None:
            result['sqlStatementContents'] = self.sql_statement_contents.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sqlStatementContents') is not None:
            temp_model = main_models.ListSqlStatementContentsResponseBodySqlStatementContents()
            self.sql_statement_contents = temp_model.from_map(m.get('sqlStatementContents'))

        return self

class ListSqlStatementContentsResponseBodySqlStatementContents(DaraModel):
    def __init__(
        self,
        contents: str = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.contents = contents
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contents is not None:
            result['contents'] = self.contents

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contents') is not None:
            self.contents = m.get('contents')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

