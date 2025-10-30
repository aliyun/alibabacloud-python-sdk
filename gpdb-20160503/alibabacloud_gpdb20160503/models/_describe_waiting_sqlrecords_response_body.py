# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeWaitingSQLRecordsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeWaitingSQLRecordsResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of lock diagnostics records.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
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
                temp_model = main_models.DescribeWaitingSQLRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWaitingSQLRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        database: str = None,
        pid: str = None,
        sqlstmt: str = None,
        session_id: str = None,
        start_time: int = None,
        status: str = None,
        user: str = None,
        waiting_time: int = None,
    ):
        # The name of the database.
        self.database = database
        # The ID of the process that uniquely identifies the query.
        self.pid = pid
        # The SQL statement of the query.
        self.sqlstmt = sqlstmt
        # The ID of the session that contains the query.
        self.session_id = session_id
        # The start time of the query. This value is in the timestamp format. Unit: milliseconds.
        self.start_time = start_time
        # The waiting state of the query. Valid values:
        # 
        # *   **LockWaiting**
        # *   **ResourceWaiting**
        self.status = status
        # The database account that is used to perform the query.
        self.user = user
        # The waiting period of the query. Unit: milliseconds.
        self.waiting_time = waiting_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        if self.pid is not None:
            result['PID'] = self.pid

        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt

        if self.session_id is not None:
            result['SessionID'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user is not None:
            result['User'] = self.user

        if self.waiting_time is not None:
            result['WaitingTime'] = self.waiting_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('PID') is not None:
            self.pid = m.get('PID')

        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')

        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('WaitingTime') is not None:
            self.waiting_time = m.get('WaitingTime')

        return self

