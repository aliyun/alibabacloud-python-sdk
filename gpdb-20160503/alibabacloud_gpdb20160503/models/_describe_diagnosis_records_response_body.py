# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisRecordsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDiagnosisRecordsResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The threshold that determines whether the SQL statement must be truncated. The value is the number of characters.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
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
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDiagnosisRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiagnosisRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        database: str = None,
        duration: int = None,
        query_id: str = None,
        sqlstmt: str = None,
        sqltruncated: bool = None,
        sqltruncated_threshold: int = None,
        session_id: str = None,
        start_time: int = None,
        status: str = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # The execution duration of the query. Unit: seconds.
        self.duration = duration
        # The ID of the query. It is a unique identifier of the query.
        self.query_id = query_id
        # The SQL statement.
        self.sqlstmt = sqlstmt
        # Indicates whether the SQL statement needs to be truncated. Valid values:
        # 
        # *   **true**: The SQL statement needs to be truncated.
        # *   **false**: The SQL statement does not need to be truncated.
        self.sqltruncated = sqltruncated
        # The threshold used to determine whether an SQL statement must be truncated. The value is the number of characters.
        self.sqltruncated_threshold = sqltruncated_threshold
        # The ID of the session that contains the query.
        self.session_id = session_id
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query is complete.
        self.status = status
        # The name of the database account.
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

        if self.query_id is not None:
            result['QueryID'] = self.query_id

        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt

        if self.sqltruncated is not None:
            result['SQLTruncated'] = self.sqltruncated

        if self.sqltruncated_threshold is not None:
            result['SQLTruncatedThreshold'] = self.sqltruncated_threshold

        if self.session_id is not None:
            result['SessionID'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')

        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')

        if m.get('SQLTruncated') is not None:
            self.sqltruncated = m.get('SQLTruncated')

        if m.get('SQLTruncatedThreshold') is not None:
            self.sqltruncated_threshold = m.get('SQLTruncatedThreshold')

        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

