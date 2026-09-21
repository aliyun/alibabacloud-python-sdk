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
        # A reserved parameter.
        self.console_context = console_context
        # The end date of the query. Format: <i>yyyyMMdd</i> (UTC).
        # 
        # - If this parameter is left empty, the default value is the day before the current date.
        # - You can only query data from the day before the current date or earlier. The interval between the start date and the end date cannot exceed 30 days.
        self.end_dt = end_dt
        # The database engine. Valid values:
        # 
        # - **MySQL**: RDS MySQL.
        # - **PolarDBMySQL**: PolarDB for MySQL.
        self.engine = engine
        # The instance ID.
        # >Only RDS MySQL and PolarDB for MySQL instances are supported.
        self.instance_ids = instance_ids
        # The region to which the instance belongs. Valid values:
        # 
        # - **cn-china**: the Chinese mainland.
        # - **cn-hongkong**: Hong Kong (China).
        # - **ap-southeast-1**: Singapore.
        # 
        # This parameter takes effect only when the **InstanceIds** request parameter is left empty. If **InstanceIds** is left empty, data is retrieved based on the region specified by the **Region** parameter. The default region is **cn-china**. If **InstanceIds** is not empty, data is retrieved based on the region of the first instance specified by **InstanceIds**, even if the **Region** parameter is set.
        # 
        # > For instances created in regions within the Chinese mainland, set this parameter to **cn-china**.
        self.region = region
        # The start date of the query. Format: <i>yyyyMMdd</i> (UTC).
        # 
        # - If this parameter is left empty, the default value is the day before the current date.
        # - You can only query data from the day before the current date or earlier.
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

