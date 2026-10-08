# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLCollectorRetentionResponseBody(DaraModel):
    def __init__(
        self,
        config_value: str = None,
        request_id: str = None,
    ):
        # Log retention period of SQL Explorer logs. Valid values:
        # * **30**: 30 days.
        # * **180**: 180 days.
        # * **365**: 1 year.
        # * **1095**: 3 years.
        # * **1825**: 5 years.
        # 
        # > Log retention period of SQL Explorer logs for ApsaraDB RDS for PostgreSQL and ApsaraDB RDS for SQL Server is fixed at 30 days.
        self.config_value = config_value
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

