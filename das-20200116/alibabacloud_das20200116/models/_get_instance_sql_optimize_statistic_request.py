# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceSqlOptimizeStatisticRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        filter_enable: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
        threshold: str = None,
        use_merging: str = None,
    ):
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies whether to filter instances for which DAS Enterprise Edition is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If you set this parameter to **true**, only database instances for which DAS Enterprise Edition is disabled are queried. If you set this parameter to **false**, all database instances are queried.
        self.filter_enable = filter_enable
        # The database instance ID.
        # 
        # >  The database instance must be an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  For ApsaraDB RDS for MySQL Cluster Edition instances or PolarDB for MySQL clusters, you must specify the node ID.
        self.node_id = node_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The duration threshold for automatic SQL optimization events. After this parameter is specified, the system collects statistics on automatic SQL optimization events whose duration does not exceed the specified threshold.
        # 
        # >  This parameter is a reserved parameter and does not take effect.
        self.threshold = threshold
        # Specifies whether to merge automatic SQL optimization events. Valid values:
        # 
        # *   **true**: merges automatic SQL optimization events.
        # *   **false**: does not merge automatic SQL optimization events.
        # 
        # >  This parameter is a reserved parameter and does not take effect.
        self.use_merging = use_merging

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.filter_enable is not None:
            result['FilterEnable'] = self.filter_enable

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.use_merging is not None:
            result['UseMerging'] = self.use_merging

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FilterEnable') is not None:
            self.filter_enable = m.get('FilterEnable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('UseMerging') is not None:
            self.use_merging = m.get('UseMerging')

        return self

