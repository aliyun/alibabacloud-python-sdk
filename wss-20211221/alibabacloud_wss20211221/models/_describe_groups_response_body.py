# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.DescribeGroupsResponseBodyGroups] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of groups.
        self.groups = groups
        # The pagination token. Leave this parameter empty for the first request. For subsequent requests, use the `nextToken` value returned in the previous response.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_count: int = None,
        instances: List[main_models.DescribeGroupsResponseBodyGroupsInstances] = None,
        last_week_used_core_time: float = None,
        left_core_time: float = None,
        resource_ids: List[str] = None,
        total_time_decimal: str = None,
        used_core_time: float = None,
        used_time_decimal: str = None,
    ):
        # The group ID.
        self.group_id = group_id
        # The number of instances.
        self.instance_count = instance_count
        # The list of instance information.
        self.instances = instances
        # The core-hour usage in the last week.
        self.last_week_used_core_time = last_week_used_core_time
        # The remaining core-hours.
        self.left_core_time = left_core_time
        # The list of resource IDs.
        self.resource_ids = resource_ids
        # The total duration with a precision factor.
        self.total_time_decimal = total_time_decimal
        # The used core-hours.
        self.used_core_time = used_core_time
        # The usage duration with a precision factor.
        self.used_time_decimal = used_time_decimal

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.last_week_used_core_time is not None:
            result['LastWeekUsedCoreTime'] = self.last_week_used_core_time

        if self.left_core_time is not None:
            result['LeftCoreTime'] = self.left_core_time

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.total_time_decimal is not None:
            result['TotalTimeDecimal'] = self.total_time_decimal

        if self.used_core_time is not None:
            result['UsedCoreTime'] = self.used_core_time

        if self.used_time_decimal is not None:
            result['UsedTimeDecimal'] = self.used_time_decimal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeGroupsResponseBodyGroupsInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('LastWeekUsedCoreTime') is not None:
            self.last_week_used_core_time = m.get('LastWeekUsedCoreTime')

        if m.get('LeftCoreTime') is not None:
            self.left_core_time = m.get('LeftCoreTime')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('TotalTimeDecimal') is not None:
            self.total_time_decimal = m.get('TotalTimeDecimal')

        if m.get('UsedCoreTime') is not None:
            self.used_core_time = m.get('UsedCoreTime')

        if m.get('UsedTimeDecimal') is not None:
            self.used_time_decimal = m.get('UsedTimeDecimal')

        return self

class DescribeGroupsResponseBodyGroupsInstances(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        expired_time: str = None,
        free_trial: bool = None,
        group_resource_type: str = None,
        instance_id: str = None,
        period: int = None,
        period_end_time: str = None,
        period_start_time: str = None,
        period_unit: str = None,
        priority_deduction: bool = None,
        resource_type: str = None,
        start_time: str = None,
        state: str = None,
        total_time: int = None,
        total_time_decimal: str = None,
        usage_alert_rule: main_models.DescribeGroupsResponseBodyGroupsInstancesUsageAlertRule = None,
        used_time: int = None,
        used_time_decimal: str = None,
    ):
        # The Alibaba Cloud user ID.
        self.ali_uid = ali_uid
        # The expiration time. The time is in ISO 8601 format and the UTC time zone.
        self.expired_time = expired_time
        # Specifies whether the instance is on a free trial.
        self.free_trial = free_trial
        # The group resource type.
        self.group_resource_type = group_resource_type
        # The instance ID.
        self.instance_id = instance_id
        # The purchase period.
        self.period = period
        # The end time of the current period. The time is in the YYYY-MM-DD HH:mm:ss format.
        self.period_end_time = period_end_time
        # The start time of the current period. The time is in the YYYY-MM-DD HH:mm:ss format.
        self.period_start_time = period_start_time
        # The period unit.
        self.period_unit = period_unit
        # Specifies whether priority deduction is enabled.
        self.priority_deduction = priority_deduction
        # The resource type.
        self.resource_type = resource_type
        # The start time. The time is in ISO 8601 format and the UTC time zone.
        self.start_time = start_time
        # The state.
        self.state = state
        # The total duration.
        self.total_time = total_time
        # The total duration with a precision factor.
        self.total_time_decimal = total_time_decimal
        # The usage Threshold Alerting rule.
        self.usage_alert_rule = usage_alert_rule
        # The usage duration.
        self.used_time = used_time
        # The usage duration with a precision factor.
        self.used_time_decimal = used_time_decimal

    def validate(self):
        if self.usage_alert_rule:
            self.usage_alert_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.free_trial is not None:
            result['FreeTrial'] = self.free_trial

        if self.group_resource_type is not None:
            result['GroupResourceType'] = self.group_resource_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_end_time is not None:
            result['PeriodEndTime'] = self.period_end_time

        if self.period_start_time is not None:
            result['PeriodStartTime'] = self.period_start_time

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.priority_deduction is not None:
            result['PriorityDeduction'] = self.priority_deduction

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.total_time_decimal is not None:
            result['TotalTimeDecimal'] = self.total_time_decimal

        if self.usage_alert_rule is not None:
            result['UsageAlertRule'] = self.usage_alert_rule.to_map()

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.used_time_decimal is not None:
            result['UsedTimeDecimal'] = self.used_time_decimal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FreeTrial') is not None:
            self.free_trial = m.get('FreeTrial')

        if m.get('GroupResourceType') is not None:
            self.group_resource_type = m.get('GroupResourceType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodEndTime') is not None:
            self.period_end_time = m.get('PeriodEndTime')

        if m.get('PeriodStartTime') is not None:
            self.period_start_time = m.get('PeriodStartTime')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PriorityDeduction') is not None:
            self.priority_deduction = m.get('PriorityDeduction')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('TotalTimeDecimal') is not None:
            self.total_time_decimal = m.get('TotalTimeDecimal')

        if m.get('UsageAlertRule') is not None:
            temp_model = main_models.DescribeGroupsResponseBodyGroupsInstancesUsageAlertRule()
            self.usage_alert_rule = temp_model.from_map(m.get('UsageAlertRule'))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('UsedTimeDecimal') is not None:
            self.used_time_decimal = m.get('UsedTimeDecimal')

        return self

class DescribeGroupsResponseBodyGroupsInstancesUsageAlertRule(DaraModel):
    def __init__(
        self,
        contact_group_names: List[str] = None,
        last_triggered_at: str = None,
        threshold_percent: int = None,
    ):
        # The list of contact group names.
        self.contact_group_names = contact_group_names
        # The last trigger time.
        self.last_triggered_at = last_triggered_at
        # The percentage of the quota alert threshold.
        self.threshold_percent = threshold_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_names is not None:
            result['ContactGroupNames'] = self.contact_group_names

        if self.last_triggered_at is not None:
            result['LastTriggeredAt'] = self.last_triggered_at

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupNames') is not None:
            self.contact_group_names = m.get('ContactGroupNames')

        if m.get('LastTriggeredAt') is not None:
            self.last_triggered_at = m.get('LastTriggeredAt')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        return self

