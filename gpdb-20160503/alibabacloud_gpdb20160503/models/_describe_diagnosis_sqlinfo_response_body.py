# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosisSQLInfoResponseBody(DaraModel):
    def __init__(
        self,
        database: str = None,
        duration: int = None,
        max_output_rows: str = None,
        query_id: str = None,
        query_plan: str = None,
        request_id: str = None,
        sqlstmt: str = None,
        session_id: str = None,
        sorted_metrics: str = None,
        start_time: int = None,
        status: str = None,
        text_plan: str = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # The execution duration of the query. Unit: seconds.
        self.duration = duration
        # The maximum number of output rows.
        self.max_output_rows = max_output_rows
        # The query ID.
        self.query_id = query_id
        # The information about the operator.
        self.query_plan = query_plan
        # The request ID.
        self.request_id = request_id
        # The SQL statement.
        self.sqlstmt = sqlstmt
        # The ID of the session that contains the query.
        self.session_id = session_id
        # The sequence of metrics.
        self.sorted_metrics = sorted_metrics
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The execution state of the query. Valid values:
        # 
        # *   **running**
        # *   **finished**
        self.status = status
        # The information about the execution plan.
        self.text_plan = text_plan
        # The username.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.max_output_rows is not None:
            result['MaxOutputRows'] = self.max_output_rows

        if self.query_id is not None:
            result['QueryID'] = self.query_id

        if self.query_plan is not None:
            result['QueryPlan'] = self.query_plan

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt

        if self.session_id is not None:
            result['SessionID'] = self.session_id

        if self.sorted_metrics is not None:
            result['SortedMetrics'] = self.sorted_metrics

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.text_plan is not None:
            result['TextPlan'] = self.text_plan

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MaxOutputRows') is not None:
            self.max_output_rows = m.get('MaxOutputRows')

        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')

        if m.get('QueryPlan') is not None:
            self.query_plan = m.get('QueryPlan')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')

        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')

        if m.get('SortedMetrics') is not None:
            self.sorted_metrics = m.get('SortedMetrics')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TextPlan') is not None:
            self.text_plan = m.get('TextPlan')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

