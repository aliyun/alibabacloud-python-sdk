# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetErrorRequestSampleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetErrorRequestSampleResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetErrorRequestSampleResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetErrorRequestSampleResponseBodyData(DaraModel):
    def __init__(
        self,
        database: str = None,
        error_code: str = None,
        instance_id: str = None,
        origin_host: str = None,
        sql: str = None,
        sql_id: str = None,
        tables: List[str] = None,
        timestamp: int = None,
        user: str = None,
    ):
        # The database name.
        self.database = database
        # The error code that is returned.
        self.error_code = error_code
        # The instance ID.
        self.instance_id = instance_id
        # The IP address of the client that executes the SQL statement.
        self.origin_host = origin_host
        # The SQL statement.
        self.sql = sql
        # The SQL query ID.
        self.sql_id = sql_id
        # The table information.
        self.tables = tables
        # The time when the SQL query was executed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The username of the account that is used to log on to the database.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['database'] = self.database

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.origin_host is not None:
            result['originHost'] = self.origin_host

        if self.sql is not None:
            result['sql'] = self.sql

        if self.sql_id is not None:
            result['sqlId'] = self.sql_id

        if self.tables is not None:
            result['tables'] = self.tables

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('originHost') is not None:
            self.origin_host = m.get('originHost')

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

