# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceErrorLogResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstanceErrorLogResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The content of the error log.
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
                temp_model = main_models.DescribeDBInstanceErrorLogResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstanceErrorLogResponseBodyItems(DaraModel):
    def __init__(
        self,
        database: str = None,
        host: str = None,
        log_context: str = None,
        log_level: str = None,
        time: int = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # This parameter is not supported.
        self.host = host
        # The content of the error log.
        self.log_context = log_context
        # The level of the queried log.
        self.log_level = log_level
        # The time when the log was generated. The time is displayed in UTC.
        self.time = time
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

        if self.host is not None:
            result['Host'] = self.host

        if self.log_context is not None:
            result['LogContext'] = self.log_context

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        if self.time is not None:
            result['Time'] = self.time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('LogContext') is not None:
            self.log_context = m.get('LogContext')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

