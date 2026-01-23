# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpsertQualityScheduleRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        upsert_command: main_models.UpsertQualityScheduleRequestUpsertCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.upsert_command = upsert_command

    def validate(self):
        if self.upsert_command:
            self.upsert_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.upsert_command is not None:
            result['UpsertCommand'] = self.upsert_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpsertCommand') is not None:
            temp_model = main_models.UpsertQualityScheduleRequestUpsertCommand()
            self.upsert_command = temp_model.from_map(m.get('UpsertCommand'))

        return self

class UpsertQualityScheduleRequestUpsertCommand(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        id: int = None,
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
        self.cron_expression = cron_expression
        self.id = id
        # This parameter is required.
        self.name = name
        self.partition_expression = partition_expression
        self.partition_type = partition_type
        self.period_schedule_interval_type = period_schedule_interval_type
        self.period_schedule_param_list = period_schedule_param_list
        self.static_task_trigger_type = static_task_trigger_type
        self.trigger_node_list = trigger_node_list
        self.trigger_type = trigger_type
        # This parameter is required.
        self.type = type
        self.validate_partition_type = validate_partition_type
        # This parameter is required.
        self.watch_id = watch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.id is not None:
            result['Id'] = self.id

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
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

