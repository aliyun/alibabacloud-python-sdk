# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSavingsPlanEstimationResponseBody(DaraModel):
    def __init__(
        self,
        committed_amount: str = None,
        currency: str = None,
        instance_type_family: str = None,
        instance_type_family_group: str = None,
        offering_type: str = None,
        period: int = None,
        period_unit: str = None,
        plan_type: str = None,
        request_id: str = None,
        resource_id: str = None,
    ):
        self.committed_amount = committed_amount
        self.currency = currency
        self.instance_type_family = instance_type_family
        self.instance_type_family_group = instance_type_family_group
        self.offering_type = offering_type
        self.period = period
        self.period_unit = period_unit
        self.plan_type = plan_type
        self.request_id = request_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.committed_amount is not None:
            result['CommittedAmount'] = self.committed_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.instance_type_family_group is not None:
            result['InstanceTypeFamilyGroup'] = self.instance_type_family_group

        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommittedAmount') is not None:
            self.committed_amount = m.get('CommittedAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InstanceTypeFamilyGroup') is not None:
            self.instance_type_family_group = m.get('InstanceTypeFamilyGroup')

        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

