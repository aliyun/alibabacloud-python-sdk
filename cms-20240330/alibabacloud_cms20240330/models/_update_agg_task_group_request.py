# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateAggTaskGroupRequest(DaraModel):
    def __init__(
        self,
        agg_task_group_config: str = None,
        agg_task_group_config_type: str = None,
        agg_task_group_name: str = None,
        cron_expr: str = None,
        delay: int = None,
        description: str = None,
        from_time: int = None,
        max_retries: int = None,
        max_run_time_in_seconds: int = None,
        precheck_string: str = None,
        schedule_mode: str = None,
        schedule_time_expr: str = None,
        status: str = None,
        tags: List[main_models.UpdateAggTaskGroupRequestTags] = None,
        target_prometheus_id: str = None,
        to_time: int = None,
    ):
        # The configuration of the aggregation task group. Only the RecordingRuleYaml format is supported. The configuration must meet the format requirements of RecordingRule in open-source Prometheus.
        # 
        # This parameter is required.
        self.agg_task_group_config = agg_task_group_config
        # The configuration type of the aggregation task group. Default value: RecordingRuleYaml, which is the RecordingRule format of open-source Prometheus.
        self.agg_task_group_config_type = agg_task_group_config_type
        # The name of the aggregation task group.
        self.agg_task_group_name = agg_task_group_name
        # The cron expression used when the scheduling mode is set to Cron. For example, 0/1 * * * * indicates that the task is scheduled every 1 minute starting from minute 0.
        self.cron_expr = cron_expr
        # The fixed delay time for scheduling, in seconds. Default value: 30.
        self.delay = delay
        # The description of the aggregation task group.
        self.description = description
        # The timestamp of the scheduling start time, in seconds.
        self.from_time = from_time
        # The maximum number of retries for executing the aggregation task. Default value: 20.
        self.max_retries = max_retries
        # The maximum retry time to execute the aggregation node, in seconds. Default value: 600.
        self.max_run_time_in_seconds = max_run_time_in_seconds
        # The precheck configuration. By default, this parameter is not configured. The input string must be a valid JSON string.
        self.precheck_string = precheck_string
        # The scheduling mode. Valid values: Cron and FixedRate. Default value: FixedRate.
        self.schedule_mode = schedule_mode
        # The scheduling time expression. Use @s or @m to specify the alignment granularity of the scheduling time window. Default value: @m.
        self.schedule_time_expr = schedule_time_expr
        # The status of the aggregation task group. Valid values: Running and Stopped. Default value: Running.
        self.status = status
        # The tags of the resource group.
        self.tags = tags
        # The target Prometheus instance ID of the aggregation node group.
        # 
        # This parameter is required.
        self.target_prometheus_id = target_prometheus_id
        # The timestamp of the scheduling end time, in seconds. A value of 0 indicates that the scheduling does not stop.
        self.to_time = to_time

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

        if self.agg_task_group_config_type is not None:
            result['aggTaskGroupConfigType'] = self.agg_task_group_config_type

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

        if self.schedule_mode is not None:
            result['scheduleMode'] = self.schedule_mode

        if self.schedule_time_expr is not None:
            result['scheduleTimeExpr'] = self.schedule_time_expr

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggTaskGroupConfig') is not None:
            self.agg_task_group_config = m.get('aggTaskGroupConfig')

        if m.get('aggTaskGroupConfigType') is not None:
            self.agg_task_group_config_type = m.get('aggTaskGroupConfigType')

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

        if m.get('scheduleMode') is not None:
            self.schedule_mode = m.get('scheduleMode')

        if m.get('scheduleTimeExpr') is not None:
            self.schedule_time_expr = m.get('scheduleTimeExpr')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.UpdateAggTaskGroupRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('targetPrometheusId') is not None:
            self.target_prometheus_id = m.get('targetPrometheusId')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

class UpdateAggTaskGroupRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

