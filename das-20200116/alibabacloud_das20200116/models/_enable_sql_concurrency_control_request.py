# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableSqlConcurrencyControlRequest(DaraModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        console_context: str = None,
        instance_id: str = None,
        max_concurrency: int = None,
        sql_keywords: str = None,
        sql_type: str = None,
    ):
        # The duration within which the SQL throttling rule takes effect. Unit: seconds.
        # 
        # >  The throttling rule takes effect only within this duration.
        # 
        # This parameter is required.
        self.concurrency_control_time = concurrency_control_time
        # The reserved parameter.
        self.console_context = console_context
        # The instance ID.
        # 
        # >  You must specify the instance ID only if your database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of concurrent SQL statements. Set this parameter to a positive integer.
        # 
        # >  When the number of concurrent SQL statements that contain the specified keywords reaches this upper limit, the throttling rule is triggered.
        # 
        # This parameter is required.
        self.max_concurrency = max_concurrency
        # The keywords that are used to identify the SQL statements that need to be throttled.
        # 
        # >  If you specify multiple SQL keywords, separate them with tildes (~). If the number of concurrent SQL statements that contain all the specified SQL keywords reaches the specified upper limit, the throttling rule is triggered.
        # 
        # This parameter is required.
        self.sql_keywords = sql_keywords
        # The type of the SQL statements. Valid values:
        # 
        # *   **SELECT**
        # *   **UPDATE**
        # *   **DELETE**
        # 
        # This parameter is required.
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time

        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')

        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        return self

