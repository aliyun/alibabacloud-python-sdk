# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAggTaskGroupStatusResponseBody(DaraModel):
    def __init__(
        self,
        agg_task_group_config_hash: str = None,
        agg_task_group_id: str = None,
        agg_task_group_name: str = None,
        request_id: str = None,
        source_prometheus_id: str = None,
        status: str = None,
    ):
        # Summary of the aggregation task group configuration.
        self.agg_task_group_config_hash = agg_task_group_config_hash
        # Aggregation task group ID.
        self.agg_task_group_id = agg_task_group_id
        # Aggregation task group name.
        self.agg_task_group_name = agg_task_group_name
        # Request ID.
        self.request_id = request_id
        # Source Prometheus instance ID of the aggregation task group.
        self.source_prometheus_id = source_prometheus_id
        # The current status of the aggregated task group.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_task_group_config_hash is not None:
            result['aggTaskGroupConfigHash'] = self.agg_task_group_config_hash

        if self.agg_task_group_id is not None:
            result['aggTaskGroupId'] = self.agg_task_group_id

        if self.agg_task_group_name is not None:
            result['aggTaskGroupName'] = self.agg_task_group_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_prometheus_id is not None:
            result['sourcePrometheusId'] = self.source_prometheus_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggTaskGroupConfigHash') is not None:
            self.agg_task_group_config_hash = m.get('aggTaskGroupConfigHash')

        if m.get('aggTaskGroupId') is not None:
            self.agg_task_group_id = m.get('aggTaskGroupId')

        if m.get('aggTaskGroupName') is not None:
            self.agg_task_group_name = m.get('aggTaskGroupName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourcePrometheusId') is not None:
            self.source_prometheus_id = m.get('sourcePrometheusId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

