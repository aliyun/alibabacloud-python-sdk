# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveSQLRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        queries: List[main_models.DescribeActiveSQLRecordsResponseBodyQueries] = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The queried SQL records.
        self.queries = queries
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.queries:
            for v1 in self.queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['Queries'] = []
        if self.queries is not None:
            for k1 in self.queries:
                result['Queries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.queries = []
        if m.get('Queries') is not None:
            for k1 in m.get('Queries'):
                temp_model = main_models.DescribeActiveSQLRecordsResponseBodyQueries()
                self.queries.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeActiveSQLRecordsResponseBodyQueries(DaraModel):
    def __init__(
        self,
        client_addr: str = None,
        database: str = None,
        pid: str = None,
        query: str = None,
        query_duration: str = None,
        query_start: str = None,
        session_id: str = None,
        sql_truncated: str = None,
        sql_truncated_threshold: str = None,
        state: str = None,
        user: str = None,
    ):
        # The IP address of the client.
        self.client_addr = client_addr
        # The name of the database.
        self.database = database
        # The progress ID.
        self.pid = pid
        # The SQL statement of the query.
        self.query = query
        # The execution duration of the query. Unit: seconds.
        self.query_duration = query_duration
        # The start time of the query.
        self.query_start = query_start
        # The session ID.
        self.session_id = session_id
        # Indicates whether the SQL statement is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.sql_truncated = sql_truncated
        # The threshold that is used to truncate the SQL statement.
        self.sql_truncated_threshold = sql_truncated_threshold
        # The status of the asynchronous request. Valid values:
        # 
        # *   **running**
        # *   **block**
        self.state = state
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr

        if self.database is not None:
            result['Database'] = self.database

        if self.pid is not None:
            result['PID'] = self.pid

        if self.query is not None:
            result['Query'] = self.query

        if self.query_duration is not None:
            result['QueryDuration'] = self.query_duration

        if self.query_start is not None:
            result['QueryStart'] = self.query_start

        if self.session_id is not None:
            result['SessionID'] = self.session_id

        if self.sql_truncated is not None:
            result['SqlTruncated'] = self.sql_truncated

        if self.sql_truncated_threshold is not None:
            result['SqlTruncatedThreshold'] = self.sql_truncated_threshold

        if self.state is not None:
            result['State'] = self.state

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('PID') is not None:
            self.pid = m.get('PID')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryDuration') is not None:
            self.query_duration = m.get('QueryDuration')

        if m.get('QueryStart') is not None:
            self.query_start = m.get('QueryStart')

        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')

        if m.get('SqlTruncated') is not None:
            self.sql_truncated = m.get('SqlTruncated')

        if m.get('SqlTruncatedThreshold') is not None:
            self.sql_truncated_threshold = m.get('SqlTruncatedThreshold')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

