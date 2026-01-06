# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSqlOptimizeAdviceRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        end_dt: str = None,
        engine: str = None,
        instance_ids: str = None,
        region: str = None,
        start_dt: str = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The end date of the time range to query. Specify the date in the *yyyyMMdd* format. The time must be in UTC.
        # 
        # *   The default value of this parameter is one day before the current day.
        # *   The value must be earlier than the current day. The interval between the start date and the end date cannot exceed 30 days.
        self.end_dt = end_dt
        # The database engine. Valid values:
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL.
        # *   **PolarDBMySQL**: PolarDB for MySQL.
        self.engine = engine
        # The instance ID.
        # 
        # >  You must specify the instance ID only if your database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        self.instance_ids = instance_ids
        # The region in which the instance resides. Valid values:
        # 
        # *   **cn-china**: Chinese mainland.
        # *   **cn-hongkong**: China (Hong Kong).
        # *   **ap-southeast-1**: Singapore.
        # 
        # This parameter takes effect only if **InstanceIds** is left empty. If you leave **InstanceIds** empty, the system obtains data from the region specified by **Region**. By default, Region is set to **cn-china**. If you specify **InstanceIds**, **Region** does not take effect, and the system obtains data from the region in which the first specified instance resides.****
        # 
        # >  If your instances reside in the regions inside the Chinese mainland, set this parameter to **cn-china**.
        self.region = region
        # The start date of the time range to query. Specify the date in the *yyyyMMdd* format. The time must be in UTC.
        # 
        # *   The default value of this parameter is one day before the current day.
        # *   The value must be earlier than the current day.
        self.start_dt = start_dt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.end_dt is not None:
            result['EndDt'] = self.end_dt

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region is not None:
            result['Region'] = self.region

        if self.start_dt is not None:
            result['StartDt'] = self.start_dt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('EndDt') is not None:
            self.end_dt = m.get('EndDt')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartDt') is not None:
            self.start_dt = m.get('StartDt')

        return self

