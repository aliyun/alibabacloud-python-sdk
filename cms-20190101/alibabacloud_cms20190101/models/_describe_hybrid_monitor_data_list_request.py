# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridMonitorDataListRequest(DaraModel):
    def __init__(
        self,
        end: int = None,
        namespace: str = None,
        period: str = None,
        prom_sql: str = None,
        region_id: str = None,
        start: int = None,
    ):
        # The end of the time range to query.
        # 
        # Unit: seconds.
        # 
        # This parameter is required.
        self.end = end
        # The name of the namespace.
        # 
        # For more information about how to query the names of namespaces, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The statistical period of the monitoring data.
        # 
        # Unit: seconds.
        self.period = period
        # The metric name.
        # 
        # >  PromQL statements are supported.
        # 
        # This parameter is required.
        self.prom_sql = prom_sql
        self.region_id = region_id
        # The start of the time range to query.
        # 
        # Unit: seconds.
        # 
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.period is not None:
            result['Period'] = self.period

        if self.prom_sql is not None:
            result['PromSQL'] = self.prom_sql

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromSQL') is not None:
            self.prom_sql = m.get('PromSQL')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

