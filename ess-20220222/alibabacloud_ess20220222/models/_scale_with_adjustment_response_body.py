# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ScaleWithAdjustmentResponseBody(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        plan_result: main_models.ScaleWithAdjustmentResponseBodyPlanResult = None,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        # The type of the scaling activity.
        # 
        # If this parameter is set to `CapacityChange`, the scaling activity only adjusts the desired capacity of the scaling group without immediately adding or removing instances.
        # 
        # This setting only affects scaling groups with a configured desired capacity.
        self.activity_type = activity_type
        # The scaling plan result returned when ExecutionMode is set to PlanOnly.
        self.plan_result = plan_result
        # The request ID.
        self.request_id = request_id
        # The ID of the scaling activity.
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        if self.plan_result:
            self.plan_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.plan_result is not None:
            result['PlanResult'] = self.plan_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('PlanResult') is not None:
            temp_model = main_models.ScaleWithAdjustmentResponseBodyPlanResult()
            self.plan_result = temp_model.from_map(m.get('PlanResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        return self

class ScaleWithAdjustmentResponseBodyPlanResult(DaraModel):
    def __init__(
        self,
        resource_allocations: List[main_models.ScaleWithAdjustmentResponseBodyPlanResultResourceAllocations] = None,
    ):
        # The resource allocation details in the scaling plan result.
        self.resource_allocations = resource_allocations

    def validate(self):
        if self.resource_allocations:
            for v1 in self.resource_allocations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceAllocations'] = []
        if self.resource_allocations is not None:
            for k1 in self.resource_allocations:
                result['ResourceAllocations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_allocations = []
        if m.get('ResourceAllocations') is not None:
            for k1 in m.get('ResourceAllocations'):
                temp_model = main_models.ScaleWithAdjustmentResponseBodyPlanResultResourceAllocations()
                self.resource_allocations.append(temp_model.from_map(k1))

        return self

class ScaleWithAdjustmentResponseBodyPlanResultResourceAllocations(DaraModel):
    def __init__(
        self,
        amount: int = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        spot_strategy: str = None,
        zone_id: str = None,
    ):
        # The number of instances.
        self.amount = amount
        # The billing method of the instance. Valid values:
        # 
        # - **Prepaid**: subscription
        # 
        # - **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The instance type.
        self.instance_type = instance_type
        # The spot strategy of the instance. Valid values:
        # 
        # - NoSpot: A pay-as-you-go instance.
        # 
        # - SpotWithPriceLimit: A spot instance with a user-specified price limit.
        # 
        # - SpotAsPriceGo: A spot instance where the system automatically bids based on the current market price.
        self.spot_strategy = spot_strategy
        # The availability zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

