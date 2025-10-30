# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceErrorLogRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        host: str = None,
        keywords: str = None,
        log_level: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        user: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # This parameter is not supported in Alibaba Cloud public cloud.
        self.host = host
        # One or more keywords that are used to query error logs.
        self.keywords = keywords
        # The level of the logs to query. Valid values:
        # 
        # *   **ALL**: queries all error logs.
        # *   **PANIC**: queries only abnormal logs.
        # *   **FATAL**: queries only critical logs.
        # *   **ERROR**: queries only error logs.
        self.log_level = log_level
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **20**
        # *   **50**
        # *   **100**
        # 
        # Default value: **20**.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time
        # The username.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database is not None:
            result['Database'] = self.database

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.host is not None:
            result['Host'] = self.host

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

