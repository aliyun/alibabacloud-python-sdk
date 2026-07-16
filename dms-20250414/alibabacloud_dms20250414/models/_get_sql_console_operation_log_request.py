# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSqlConsoleOperationLogRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: int = None,
        page_number: int = None,
        page_size: int = None,
        schema: str = None,
        sql_type: str = None,
        start_time: str = None,
        username: str = None,
    ):
        # The end time of the logs.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The database schema.
        self.schema = schema
        # The type of the SQL statement.
        self.sql_type = sql_type
        # The start time of the logs.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

