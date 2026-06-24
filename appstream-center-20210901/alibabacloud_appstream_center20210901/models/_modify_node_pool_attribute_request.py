# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyNodePoolAttributeRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        node_capacity: int = None,
        node_pool_strategy: main_models.ModifyNodePoolAttributeRequestNodePoolStrategy = None,
        pool_id: str = None,
        product_type: str = None,
    ):
        # The region ID of the delivery group. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        self.biz_region_id = biz_region_id
        # The number of concurrent sessions, which is the number of sessions that can be simultaneously connected to a single resource. If too many sessions are connected simultaneously, the application experience may degrade. The valid values vary depending on the resource specification. The valid values for each resource specification are as follows:
        # 
        # - appstreaming.general.4c8g: 1 to 2.
        # - appstreaming.general.8c16g: 1 to 4.
        # - appstreaming.vgpu.8c16g.4g: 1 to 4.
        # - appstreaming.vgpu.8c31g.16g: 1 to 4.
        # - appstreaming.vgpu.14c93g.12g: 1 to 6.
        self.node_capacity = node_capacity
        # The automatic scaling policy of the delivery group.
        self.node_pool_strategy = node_pool_strategy
        # The resource group ID.
        self.pool_id = pool_id
        # The product type.
        self.product_type = product_type

    def validate(self):
        if self.node_pool_strategy:
            self.node_pool_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity

        if self.node_pool_strategy is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy.to_map()

        if self.pool_id is not None:
            result['PoolId'] = self.pool_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')

        if m.get('NodePoolStrategy') is not None:
            temp_model = main_models.ModifyNodePoolAttributeRequestNodePoolStrategy()
            self.node_pool_strategy = temp_model.from_map(m.get('NodePoolStrategy'))

        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

class ModifyNodePoolAttributeRequestNodePoolStrategy(DaraModel):
    def __init__(
        self,
        max_idle_app_instance_amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        recurrence_schedules: List[main_models.ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        # The maximum number of idle sessions. When this value is specified, automatic scale-out is triggered only when the session usage exceeds `ScalingUsageThreshold` and the number of idle sessions in the current delivery group is less than `MaxIdleAppInstanceAmount`. Otherwise, the idle sessions in the delivery group are considered sufficient, and no automatic scale-out is performed. This parameter can be used to flexibly control elastic scale-out behavior and reduce costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created during scale-out. This parameter is required when `StrategyType` is set to `NODE_SCALING_BY_USAGE`.
        self.max_scaling_amount = max_scaling_amount
        # The number of purchased resources. Valid values: 1 to 100.
        # 
        # > 
        # - If the resources are subscription resources, this parameter cannot be modified.
        # - If the resources are pay-as-you-go resources, this parameter can be modified when the scaling mode (`StrategyType`) is set to fixed quantity (`NODE_FIXED`) or automatic scaling (`NODE_SCALING_BY_USAGE`).
        self.node_amount = node_amount
        # The list of policy execution cycles. This parameter is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.recurrence_schedules = recurrence_schedules
        # The maximum duration (in minutes) that a resource without session connections is retained. When no sessions are connected to a resource, a countdown starts based on the duration specified here. The resource is scaled in when the countdown ends. Valid values: 5 to 120. Default value: 5. The following exceptions apply:
        # 
        # - If scale-in would trigger automatic scale-out again, the scale-in is not performed to avoid repeated scale-in and scale-out operations.
        # - If automatic scale-out is triggered by an increase in sessions during this period, the resource is not scaled in as originally planned, and the countdown restarts.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of resources created per scale-out operation. Valid values: 1 to 10. This parameter is required when `StrategyType` is set to `NODE_SCALING_BY_USAGE`.
        self.scaling_step = scaling_step
        # The upper threshold of session usage (%). Automatic scale-out is triggered when the session usage exceeds this threshold. The session usage is calculated by using the following formula: `Session usage = Current sessions ÷ (Total resources × Concurrent sessions per resource) × 100%`. This parameter is required when `StrategyType` is set to `NODE_SCALING_BY_USAGE`. Valid values: 0 to 100. Default value: 85.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The date when the policy expires. Format: yyyy-MM-dd. The interval between the expiration date and the effective date must be between 7 days and 1 year, inclusive. This parameter is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.strategy_disable_date = strategy_disable_date
        # The date when the policy takes effect. Format: yyyy-MM-dd. The date must be equal to or later than the current date. This parameter is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.strategy_enable_date = strategy_enable_date
        # The scaling mode.
        # 
        # > 
        # - `NODE_FIXED` (fixed quantity): Applicable to subscription and pay-as-you-go resources.
        # - `NODE_SCALING_BY_USAGE` (automatic scaling): Applicable to subscription and pay-as-you-go resources.
        # - `NODE_SCALING_BY_SCHEDULE` (scheduled scaling): Applicable only to pay-as-you-go resources.
        self.strategy_type = strategy_type
        # Specifies whether to enable the resource prefetch policy. This parameter is required when `StrategyType` (scaling mode) is set to `NODE_SCALING_BY_SCHEDULE` (scheduled scaling).
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for v1 in self.recurrence_schedules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_idle_app_instance_amount is not None:
            result['MaxIdleAppInstanceAmount'] = self.max_idle_app_instance_amount

        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount

        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount

        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k1 in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k1.to_map() if k1 else None)

        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes

        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step

        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold

        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date

        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxIdleAppInstanceAmount') is not None:
            self.max_idle_app_instance_amount = m.get('MaxIdleAppInstanceAmount')

        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')

        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')

        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k1 in m.get('RecurrenceSchedules'):
                temp_model = main_models.ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k1))

        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')

        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')

        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')

        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')

        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')

        return self

class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules(DaraModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[main_models.ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods] = None,
    ):
        # The type of the policy execution cycle. You must specify both `RecurrenceType` and `RecurrenceValues`.
        self.recurrence_type = recurrence_type
        # The list of values for the policy execution cycle.
        self.recurrence_values = recurrence_values
        # The list of time periods for the policy execution cycle. Requirements for time period settings:
        # 
        # - You can add up to three time periods.
        # - Time periods must not overlap.
        # - The interval between time periods must be at least 5 minutes.
        # - Each time period must be at least 15 minutes long.
        # - All time periods combined must not span across days.
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for v1 in self.timer_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values

        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k1 in self.timer_periods:
                result['TimerPeriods'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')

        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k1 in m.get('TimerPeriods'):
                temp_model = main_models.ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k1))

        return self

class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods(DaraModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The resource count.
        self.amount = amount
        # The end time. Format: HH:mm.
        self.end_time = end_time
        # The start time. Format: HH:mm.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

