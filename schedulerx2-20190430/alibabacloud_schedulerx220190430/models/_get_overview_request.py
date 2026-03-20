# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOverviewRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        group_id: str = None,
        metric_type: int = None,
        namespace: str = None,
        namespace_source: str = None,
        operate: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value must be a UNIX timestamp (in seconds). If left empty, the current time is used.
        self.end_time = end_time
        # The application group ID.
        self.group_id = group_id
        # The metric type. Valid values:
        # 
        # *   0: the basic job data.
        # *   1: the job running data.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The unique identifier (UID) of the namespace.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The query type. Valid values:
        # 
        # *   query: queries data in a time range.
        # *   query_range: queries time series data in a time range.
        # 
        # This parameter is required.
        self.operate = operate
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. The value must be a UNIX timestamp (in seconds).
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

