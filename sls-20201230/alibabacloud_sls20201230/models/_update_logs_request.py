# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLogsRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        from_: int = None,
        query: str = None,
        row_id: str = None,
        to: int = None,
        update_mode: str = None,
    ):
        # The data to be updated, in JSON format.
        self.data = data
        # The start time of the query. This time refers to the log time specified when the log data was written.
        # 
        # The time range defined by the request parameters from and to follows the left-closed, right-open principle. That is, the time range includes the start time but does not include the end time. If the values of from and to are the same, the range is invalid and the function returns an error directly.
        # Unix timestamp format, representing the number of seconds since 1970-01-01 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # Optional: A query statement used to filter the logs to be updated. For more information, see [Query overview](https://help.aliyun.com/document_detail/43772.html).
        # 
        # Note: This parameter only supports query statements and does not support analysis statements such as SPL or SQL.
        self.query = query
        # Optional: The value of the built-in field __rowid__ that is automatically returned in the query results.
        # 
        # One of the two fields, rowId and query, must be specified. If both are specified, rowId takes higher priority.
        self.row_id = row_id
        # The end time of the query. This time refers to the log time specified when the log data was written.
        # 
        # The time range defined by the request parameters from and to follows the left-closed, right-open principle. That is, the time range includes the start time but does not include the end time. If the values of from and to are the same, the range is invalid and the function returns an error directly.
        # Unix timestamp format, representing the number of seconds since 1970-01-01 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # Optional: The value can be full or partial. The default value is partial.
        #   - full —— The request body must contain all fields of the row. The server overwrites the entire old record with the new values.
        #   - partial —— The request body only needs to contain the fields to be modified. Fields that are not provided retain their original values.
        self.update_mode = update_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.from_ is not None:
            result['from'] = self.from_

        if self.query is not None:
            result['query'] = self.query

        if self.row_id is not None:
            result['rowId'] = self.row_id

        if self.to is not None:
            result['to'] = self.to

        if self.update_mode is not None:
            result['updateMode'] = self.update_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('rowId') is not None:
            self.row_id = m.get('rowId')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('updateMode') is not None:
            self.update_mode = m.get('updateMode')

        return self

