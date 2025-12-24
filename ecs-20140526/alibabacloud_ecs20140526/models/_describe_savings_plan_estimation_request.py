# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSavingsPlanEstimationRequest(DaraModel):
    def __init__(
        self,
        estimation_resource: str = None,
        instance_type_scope: str = None,
        offering_type: str = None,
        period: str = None,
        period_unit: str = None,
        plan_type: str = None,
        region_id: str = None,
        resource_id: str = None,
    ):
        self.estimation_resource = estimation_resource
        self.instance_type_scope = instance_type_scope
        self.offering_type = offering_type
        self.period = period
        self.period_unit = period_unit
        self.plan_type = plan_type
        self.region_id = region_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.estimation_resource is not None:
            result['EstimationResource'] = self.estimation_resource

        if self.instance_type_scope is not None:
            result['InstanceTypeScope'] = self.instance_type_scope

        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimationResource') is not None:
            self.estimation_resource = m.get('EstimationResource')

        if m.get('InstanceTypeScope') is not None:
            self.instance_type_scope = m.get('InstanceTypeScope')

        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

