# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppNetworkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The ID of the cluster to which the container belongs.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The end timestamp of the query. Unit: milliseconds.
        # 
        # > The days between the start timestamp and the end timestamp cannot exceed **seven** days.
        self.end_time = end_time
        # The start timestamp of the query. Unit: milliseconds.
        # 
        # > The days between the start timestamp and the end timestamp cannot exceed **seven** days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

