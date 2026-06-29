# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualitySchedulesByWatchIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        quality_schedule_list: List[main_models.GetQualitySchedulesByWatchIdResponseBodyQualityScheduleList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # The list of schedule objects.
        self.quality_schedule_list = quality_schedule_list
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.quality_schedule_list:
            for v1 in self.quality_schedule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        result['QualityScheduleList'] = []
        if self.quality_schedule_list is not None:
            for k1 in self.quality_schedule_list:
                result['QualityScheduleList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.quality_schedule_list = []
        if m.get('QualityScheduleList') is not None:
            for k1 in m.get('QualityScheduleList'):
                temp_model = main_models.GetQualitySchedulesByWatchIdResponseBodyQualityScheduleList()
                self.quality_schedule_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualitySchedulesByWatchIdResponseBodyQualityScheduleList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        cron_expression: str = None,
        id: int = None,
        is_ref_by_rule: bool = None,
        modifier: str = None,
        modify_time: str = None,
        name: str = None,
        partition_expression: str = None,
        partition_type: str = None,
        period_schedule_interval_type: str = None,
        period_schedule_param_list: List[str] = None,
        static_task_trigger_type: str = None,
        trigger_node_list: List[str] = None,
        trigger_type: str = None,
        type: str = None,
        validate_partition_type: str = None,
        watch_id: int = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The user ID of the creator.
        self.creator = creator
        # The cron expression for timed scheduling.
        self.cron_expression = cron_expression
        # The schedule object ID.
        self.id = id
        # Indicates whether the schedule is referenced by a rule.
        self.is_ref_by_rule = is_ref_by_rule
        # The user ID of the last modifier.
        self.modifier = modifier
        # The modification time.
        self.modify_time = modify_time
        # The schedule object name.
        self.name = name
        # The partition expression. A custom expression.
        self.partition_expression = partition_expression
        # The partition type. Valid values:
        # - EVERY_DAY: every day.
        # - PRE_DAY: yesterday.
        # - TODAY: today.
        # - FIRST_DAY_OF_WEEK: first day of the week (Sunday).
        # - CUSTOM: custom.
        self.partition_type = partition_type
        # The interval type for timed scheduling. Valid values:
        # - DAILY: day.
        # - WEEKLY: week.
        # - MONTHLY: month.
        # - HOURLY: hour.
        # - MINUTELY: minute.
        self.period_schedule_interval_type = period_schedule_interval_type
        # The interval values for timed scheduling.
        self.period_schedule_param_list = period_schedule_param_list
        # The trigger method for fixed task triggers. Valid values:
        # - ALL_TASKS_FINISHED
        # - ONE_TASKS_FINISHED
        # - PRE_ONE_TASKS_START.
        self.static_task_trigger_type = static_task_trigger_type
        # The list of trigger nodes for trigger-based scheduling.
        self.trigger_node_list = trigger_node_list
        # The trigger method for trigger-based scheduling. Valid values:
        # - STATIC_TASK_TRIGGER: fixed task trigger.
        # - CODE_CHECK_TRIGGER: code check trigger.
        self.trigger_type = trigger_type
        # The schedule type. Valid values:
        # - PERIOD_SCHEDULE: timed scheduling.
        # - MANUAL_SCHEDULE: manual trigger.
        # - CODE_CHECK_TRIGGER: code check trigger.
        # - STATIC_TASK_TRIGGER: fixed task trigger.
        # - DEPENDENCY_SCHEDULE: dependency scheduling.
        self.type = type
        # The validation scope. Valid values:
        # - TASK_REFERRED_PARTITION: task-updated partition.
        # - USER_DEFINED_PARTITION: custom partition.
        self.validate_partition_type = validate_partition_type
        # The monitored object ID.
        self.watch_id = watch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.id is not None:
            result['Id'] = self.id

        if self.is_ref_by_rule is not None:
            result['IsRefByRule'] = self.is_ref_by_rule

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_expression is not None:
            result['PartitionExpression'] = self.partition_expression

        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type

        if self.period_schedule_interval_type is not None:
            result['PeriodScheduleIntervalType'] = self.period_schedule_interval_type

        if self.period_schedule_param_list is not None:
            result['PeriodScheduleParamList'] = self.period_schedule_param_list

        if self.static_task_trigger_type is not None:
            result['StaticTaskTriggerType'] = self.static_task_trigger_type

        if self.trigger_node_list is not None:
            result['TriggerNodeList'] = self.trigger_node_list

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.type is not None:
            result['Type'] = self.type

        if self.validate_partition_type is not None:
            result['ValidatePartitionType'] = self.validate_partition_type

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsRefByRule') is not None:
            self.is_ref_by_rule = m.get('IsRefByRule')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionExpression') is not None:
            self.partition_expression = m.get('PartitionExpression')

        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')

        if m.get('PeriodScheduleIntervalType') is not None:
            self.period_schedule_interval_type = m.get('PeriodScheduleIntervalType')

        if m.get('PeriodScheduleParamList') is not None:
            self.period_schedule_param_list = m.get('PeriodScheduleParamList')

        if m.get('StaticTaskTriggerType') is not None:
            self.static_task_trigger_type = m.get('StaticTaskTriggerType')

        if m.get('TriggerNodeList') is not None:
            self.trigger_node_list = m.get('TriggerNodeList')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValidatePartitionType') is not None:
            self.validate_partition_type = m.get('ValidatePartitionType')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

