# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetAggTaskGroupResponseBody(DaraModel):
    def __init__(
        self,
        agg_task_group: main_models.GetAggTaskGroupResponseBodyAggTaskGroup = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Aggregation task group.
        self.agg_task_group = agg_task_group
        # Request ID
        self.request_id = request_id
        # Whether the request was successful
        self.success = success

    def validate(self):
        if self.agg_task_group:
            self.agg_task_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_task_group is not None:
            result['aggTaskGroup'] = self.agg_task_group.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggTaskGroup') is not None:
            temp_model = main_models.GetAggTaskGroupResponseBodyAggTaskGroup()
            self.agg_task_group = temp_model.from_map(m.get('aggTaskGroup'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetAggTaskGroupResponseBodyAggTaskGroup(DaraModel):
    def __init__(
        self,
        agg_task_group_config: str = None,
        agg_task_group_config_hash: str = None,
        agg_task_group_id: str = None,
        agg_task_group_name: str = None,
        cron_expr: str = None,
        delay: int = None,
        description: str = None,
        from_time: int = None,
        max_retries: int = None,
        max_run_time_in_seconds: int = None,
        precheck_string: str = None,
        region_id: str = None,
        schedule_mode: str = None,
        schedule_time_expr: str = None,
        source_prometheus_id: str = None,
        status: str = None,
        tags: List[main_models.GetAggTaskGroupResponseBodyAggTaskGroupTags] = None,
        target_prometheus_id: str = None,
        to_time: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        # Aggregation task group configuration.
        self.agg_task_group_config = agg_task_group_config
        # Summary of the aggregation task group configuration.
        self.agg_task_group_config_hash = agg_task_group_config_hash
        # ID of the aggregation task group.
        self.agg_task_group_id = agg_task_group_id
        # Name of the aggregation task group.
        self.agg_task_group_name = agg_task_group_name
        # Scheduling expression for the aggregation task group when the scheduling mode is \\"Cron\\".
        self.cron_expr = cron_expr
        # Fixed delay time (in seconds) for scheduling.
        self.delay = delay
        # Description of the aggregation task group.
        self.description = description
        # Second-level timestamp corresponding to the start time of scheduling (not yet effective).
        self.from_time = from_time
        # Maximum number of retries for executing the aggregation task.
        self.max_retries = max_retries
        # Maximum retry time for executing the aggregation task.
        self.max_run_time_in_seconds = max_run_time_in_seconds
        # Pre-check configuration.
        self.precheck_string = precheck_string
        # Region ID.
        self.region_id = region_id
        # Scheduling mode.
        self.schedule_mode = schedule_mode
        # Scheduling time expression.
        self.schedule_time_expr = schedule_time_expr
        # ID of the source Prometheus instance for the aggregation task group.
        self.source_prometheus_id = source_prometheus_id
        # Status of the aggregation task group.
        self.status = status
        # Resource group tags
        self.tags = tags
        # The target Prometheus instance ID of the aggregation task group.
        self.target_prometheus_id = target_prometheus_id
        # The second-level timestamp corresponding to the end time of the scheduling.
        self.to_time = to_time
        # The update time (timestamp) of the aggregation task group.
        self.update_time = update_time
        # The user to whom the aggregation task group belongs.
        self.user_id = user_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_task_group_config is not None:
            result['aggTaskGroupConfig'] = self.agg_task_group_config

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

        if self.max_retries is not None:
            result['maxRetries'] = self.max_retries

        if self.max_run_time_in_seconds is not None:
            result['maxRunTimeInSeconds'] = self.max_run_time_in_seconds

        if self.precheck_string is not None:
            result['precheckString'] = self.precheck_string

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

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.target_prometheus_id is not None:
            result['targetPrometheusId'] = self.target_prometheus_id

        if self.to_time is not None:
            result['toTime'] = self.to_time

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggTaskGroupConfig') is not None:
            self.agg_task_group_config = m.get('aggTaskGroupConfig')

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

        if m.get('maxRetries') is not None:
            self.max_retries = m.get('maxRetries')

        if m.get('maxRunTimeInSeconds') is not None:
            self.max_run_time_in_seconds = m.get('maxRunTimeInSeconds')

        if m.get('precheckString') is not None:
            self.precheck_string = m.get('precheckString')

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

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetAggTaskGroupResponseBodyAggTaskGroupTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('targetPrometheusId') is not None:
            self.target_prometheus_id = m.get('targetPrometheusId')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetAggTaskGroupResponseBodyAggTaskGroupTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key of the resource group tag.
        self.key = key
        # The value of the resource group tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

