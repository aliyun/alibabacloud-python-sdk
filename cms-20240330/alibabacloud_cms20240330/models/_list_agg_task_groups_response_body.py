# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAggTaskGroupsResponseBody(DaraModel):
    def __init__(
        self,
        agg_task_groups: List[main_models.ListAggTaskGroupsResponseBodyAggTaskGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of aggregation task groups.
        self.agg_task_groups = agg_task_groups
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token to use to retrieve the next page of results. This value is empty when there are no more results to return.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.agg_task_groups:
            for v1 in self.agg_task_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['aggTaskGroups'] = []
        if self.agg_task_groups is not None:
            for k1 in self.agg_task_groups:
                result['aggTaskGroups'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agg_task_groups = []
        if m.get('aggTaskGroups') is not None:
            for k1 in m.get('aggTaskGroups'):
                temp_model = main_models.ListAggTaskGroupsResponseBodyAggTaskGroups()
                self.agg_task_groups.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListAggTaskGroupsResponseBodyAggTaskGroups(DaraModel):
    def __init__(
        self,
        agg_task_group_config_hash: str = None,
        agg_task_group_id: str = None,
        agg_task_group_name: str = None,
        cron_expr: str = None,
        delay: int = None,
        description: str = None,
        from_time: int = None,
        interval: str = None,
        max_retries: int = None,
        max_run_time_in_seconds: int = None,
        region_id: str = None,
        schedule_mode: str = None,
        schedule_time_expr: str = None,
        source_prometheus_id: str = None,
        status: str = None,
        target_prometheus_id: str = None,
        to_time: int = None,
        update_time: str = None,
    ):
        # The summary of the aggregation task group configuration.
        self.agg_task_group_config_hash = agg_task_group_config_hash
        # The ID of the aggregation task group.
        self.agg_task_group_id = agg_task_group_id
        # The name of the aggregation task group.
        self.agg_task_group_name = agg_task_group_name
        # The scheduling expression for the aggregation task group when the scheduling mode is \\`Cron\\`.
        self.cron_expr = cron_expr
        # The fixed delay for scheduling, in seconds.
        self.delay = delay
        # The description of the aggregation task group.
        self.description = description
        # The UNIX timestamp that indicates the scheduling start time.
        self.from_time = from_time
        # The scheduling interval.
        self.interval = interval
        # The maximum number of retries for an aggregation task.
        self.max_retries = max_retries
        # The maximum retry duration for an aggregation task, in seconds.
        self.max_run_time_in_seconds = max_run_time_in_seconds
        # The region ID.
        self.region_id = region_id
        # The scheduling mode.
        self.schedule_mode = schedule_mode
        # The scheduling time expression.
        self.schedule_time_expr = schedule_time_expr
        # The ID of the source Prometheus instance for the aggregation task group.
        self.source_prometheus_id = source_prometheus_id
        # The status of the aggregation task group.
        self.status = status
        # The ID of the target Prometheus instance for the aggregation task group.
        self.target_prometheus_id = target_prometheus_id
        # The UNIX timestamp that indicates the scheduling end time.
        self.to_time = to_time
        # The time when the aggregation task group was updated.
        self.update_time = update_time

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

        if self.cron_expr is not None:
            result['cronExpr'] = self.cron_expr

        if self.delay is not None:
            result['delay'] = self.delay

        if self.description is not None:
            result['description'] = self.description

        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.interval is not None:
            result['interval'] = self.interval

        if self.max_retries is not None:
            result['maxRetries'] = self.max_retries

        if self.max_run_time_in_seconds is not None:
            result['maxRunTimeInSeconds'] = self.max_run_time_in_seconds

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.schedule_mode is not None:
            result['scheduleMode'] = self.schedule_mode

        if self.schedule_time_expr is not None:
            result['scheduleTimeExpr'] = self.schedule_time_expr

        if self.source_prometheus_id is not None:
            result['sourcePrometheusId'] = self.source_prometheus_id

        if self.status is not None:
            result['status'] = self.status

        if self.target_prometheus_id is not None:
            result['targetPrometheusId'] = self.target_prometheus_id

        if self.to_time is not None:
            result['toTime'] = self.to_time

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggTaskGroupConfigHash') is not None:
            self.agg_task_group_config_hash = m.get('aggTaskGroupConfigHash')

        if m.get('aggTaskGroupId') is not None:
            self.agg_task_group_id = m.get('aggTaskGroupId')

        if m.get('aggTaskGroupName') is not None:
            self.agg_task_group_name = m.get('aggTaskGroupName')

        if m.get('cronExpr') is not None:
            self.cron_expr = m.get('cronExpr')

        if m.get('delay') is not None:
            self.delay = m.get('delay')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('maxRetries') is not None:
            self.max_retries = m.get('maxRetries')

        if m.get('maxRunTimeInSeconds') is not None:
            self.max_run_time_in_seconds = m.get('maxRunTimeInSeconds')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('scheduleMode') is not None:
            self.schedule_mode = m.get('scheduleMode')

        if m.get('scheduleTimeExpr') is not None:
            self.schedule_time_expr = m.get('scheduleTimeExpr')

        if m.get('sourcePrometheusId') is not None:
            self.source_prometheus_id = m.get('sourcePrometheusId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('targetPrometheusId') is not None:
            self.target_prometheus_id = m.get('targetPrometheusId')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

