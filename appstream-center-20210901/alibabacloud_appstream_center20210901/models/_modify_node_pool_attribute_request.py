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
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        # The auto scaling policy used by the delivery group.
        self.node_pool_strategy = node_pool_strategy
        self.pool_id = pool_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
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
        # The maximum number of idle sessions. After you specify a value for this parameter, auto scaling is triggered only if the number of idle sessions in the delivery group is smaller than the specified value and the session usage exceeds the value specified for `ScalingUsageThreshold`. Otherwise, the system determines that the idle sessions in the delivery group are sufficient and does not perform auto scaling.`` You can use this parameter to flexibly manage auto scaling and reduce costs.
        self.max_idle_app_instance_amount = max_idle_app_instance_amount
        # The maximum number of resources that can be created for scale-out. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_USAGE`.
        self.max_scaling_amount = max_scaling_amount
        # The number of resources to purchase. Valid values: 1 to 100.
        # 
        # > 
        # 
        # *   If you use subscription resources, you cannot modify this parameter.
        # *   If you use pay-as-you-go resources, you can modify this parameter only if you set `StrategyType` to `NODE_FIXED` or `NODE_SCALING_BY_USAGE`.
        self.node_amount = node_amount
        # The intervals at which the scaling policy is executed. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.recurrence_schedules = recurrence_schedules
        # The maximum retention period of a resource to which no session is connected. If no session is connected to a resource, the resource is automatically scaled in after the specified retention period elapses. Valid values: 5 to 120. Default value: 5. Unit: minutes. If one of the following situations occurs, the resource is not scaled in.
        # 
        # *   If a scale-out is automatically triggered after the resource is scaled in, the scale-in is not executed. This prevents repeated scale-in and scale-out.
        # *   If a scale-out is automatically triggered due to an increase in the number of sessions during the specified period of time, the resource is not scaled in and the countdown restarts.
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        # The number of resources that are created each time resources are scaled out. Valid values: 1 to 10. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_USAGE`.
        self.scaling_step = scaling_step
        # The upper limit of session usage. If the session usage exceeds the specified upper limit, auto scaling is automatically triggered. The session usage is calculated by using the following formula: `Session usage = Number of current sessions/(Total number of resources × Number of concurrent sessions) × 100%`. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_USAGE`. Valid values: 0 to 100. Default value: 85.
        self.scaling_usage_threshold = scaling_usage_threshold
        # The expiration date of the scaling policy. Format: yyyy-MM-dd. The interval between the expiration date and the effective date must be from 7 days to 1 year. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.strategy_disable_date = strategy_disable_date
        # The effective date of the scaling policy. Format: yyyy-MM-dd. The date must be the same as or later than the current date. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
        self.strategy_enable_date = strategy_enable_date
        # The scaling mode.
        # 
        # > 
        # 
        # *   `NODE_FIXED`: no scaling. This value is applicable to pay-as-you-go resources and subscription resources.
        # *   `NODE_SCALING_BY_USAGE`: auto scaling. This value is applicable to pay-as-you-go resources and subscription resources.
        # *   `NODE_SCALING_BY_SCHEDULE`: scheduled scaling. This value is applicable only to pay-as-you-go resources.
        # 
        # Valid values:
        # 
        # *   NODE_FIXED: no scaling
        # *   NODE_SCALING_BY_SCHEDULE: scheduled scaling
        # *   NODE_SCALING_BY_USAGE: auto scaling
        self.strategy_type = strategy_type
        # Specifies whether to enable the warmup policy for resources. This parameter is required only if you set `StrategyType` to `NODE_SCALING_BY_SCHEDULE`.
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
        # The schedule type of the scaling policy. This parameter must be configured together with `RecurrenceValues`.``
        # 
        # Valid values:
        # 
        # *   weekly: The scaling policy is executed on specific days each week.
        self.recurrence_type = recurrence_type
        # The days of each week on which the scaling policy is executed.
        self.recurrence_values = recurrence_values
        # The time periods during which the scaling policy can be executed. The time periods must meet the following requirements:
        # 
        # *   Up to three time periods can be added.
        # *   Time periods cannot be overlapped.
        # *   The interval between two consecutive time periods must be greater than or equal to 5 minutes.
        # *   Each time period must be greater than or equal to 15 minutes.
        # *   The total length of the time periods that you specify cannot be greater than a day.
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
        # The number of resources.
        self.amount = amount
        # The end of the time period during which the scaling policy is executed. Format: HH:mm.
        self.end_time = end_time
        # The beginning of the time period during which the scaling policy is executed. Format: HH:mm.
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

