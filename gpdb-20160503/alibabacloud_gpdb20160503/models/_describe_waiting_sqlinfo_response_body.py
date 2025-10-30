# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeWaitingSQLInfoResponseBody(DaraModel):
    def __init__(
        self,
        database: str = None,
        items: List[main_models.DescribeWaitingSQLInfoResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The name of the database.
        self.database = database
        # The queried lock-waiting query.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

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
        if self.database is not None:
            result['Database'] = self.database

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeWaitingSQLInfoResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWaitingSQLInfoResponseBodyItems(DaraModel):
    def __init__(
        self,
        application: str = None,
        blocked_by_application: str = None,
        blocked_by_pid: str = None,
        blocked_by_sqlstmt: str = None,
        blocked_by_user: str = None,
        grant_locks: str = None,
        not_grant_locks: str = None,
        pid: str = None,
        sqlstmt: str = None,
        user: str = None,
    ):
        # The application that sent the query.
        self.application = application
        # The application that sent the blocking query.
        self.blocked_by_application = blocked_by_application
        # The process ID of the blocking query.
        self.blocked_by_pid = blocked_by_pid
        # The SQL statement of the blocking query.
        self.blocked_by_sqlstmt = blocked_by_sqlstmt
        # The database account that is used to perform the blocking query.
        self.blocked_by_user = blocked_by_user
        # The authorized locks.
        self.grant_locks = grant_locks
        # The unauthorized locks.
        self.not_grant_locks = not_grant_locks
        # The ID of the process that uniquely identifies the query.
        self.pid = pid
        # The SQL statement of the query.
        self.sqlstmt = sqlstmt
        # The database account that is used to perform the query.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application

        if self.blocked_by_application is not None:
            result['BlockedByApplication'] = self.blocked_by_application

        if self.blocked_by_pid is not None:
            result['BlockedByPID'] = self.blocked_by_pid

        if self.blocked_by_sqlstmt is not None:
            result['BlockedBySQLStmt'] = self.blocked_by_sqlstmt

        if self.blocked_by_user is not None:
            result['BlockedByUser'] = self.blocked_by_user

        if self.grant_locks is not None:
            result['GrantLocks'] = self.grant_locks

        if self.not_grant_locks is not None:
            result['NotGrantLocks'] = self.not_grant_locks

        if self.pid is not None:
            result['PID'] = self.pid

        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')

        if m.get('BlockedByApplication') is not None:
            self.blocked_by_application = m.get('BlockedByApplication')

        if m.get('BlockedByPID') is not None:
            self.blocked_by_pid = m.get('BlockedByPID')

        if m.get('BlockedBySQLStmt') is not None:
            self.blocked_by_sqlstmt = m.get('BlockedBySQLStmt')

        if m.get('BlockedByUser') is not None:
            self.blocked_by_user = m.get('BlockedByUser')

        if m.get('GrantLocks') is not None:
            self.grant_locks = m.get('GrantLocks')

        if m.get('NotGrantLocks') is not None:
            self.not_grant_locks = m.get('NotGrantLocks')

        if m.get('PID') is not None:
            self.pid = m.get('PID')

        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

