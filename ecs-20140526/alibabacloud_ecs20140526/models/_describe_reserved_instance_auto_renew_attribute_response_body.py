# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeReservedInstanceAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        reserved_instance_renew_attributes: main_models.DescribeReservedInstanceAutoRenewAttributeResponseBodyReservedInstanceRenewAttributes = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Details about the auto-renewal settings of the reserved instances.
        self.reserved_instance_renew_attributes = reserved_instance_renew_attributes

    def validate(self):
        if self.reserved_instance_renew_attributes:
            self.reserved_instance_renew_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserved_instance_renew_attributes is not None:
            result['ReservedInstanceRenewAttributes'] = self.reserved_instance_renew_attributes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReservedInstanceRenewAttributes') is not None:
            temp_model = main_models.DescribeReservedInstanceAutoRenewAttributeResponseBodyReservedInstanceRenewAttributes()
            self.reserved_instance_renew_attributes = temp_model.from_map(m.get('ReservedInstanceRenewAttributes'))

        return self

class DescribeReservedInstanceAutoRenewAttributeResponseBodyReservedInstanceRenewAttributes(DaraModel):
    def __init__(
        self,
        reserved_instance_renew_attribute: List[main_models.DescribeReservedInstanceAutoRenewAttributeResponseBodyReservedInstanceRenewAttributesReservedInstanceRenewAttribute] = None,
    ):
        self.reserved_instance_renew_attribute = reserved_instance_renew_attribute

    def validate(self):
        if self.reserved_instance_renew_attribute:
            for v1 in self.reserved_instance_renew_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReservedInstanceRenewAttribute'] = []
        if self.reserved_instance_renew_attribute is not None:
            for k1 in self.reserved_instance_renew_attribute:
                result['ReservedInstanceRenewAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reserved_instance_renew_attribute = []
        if m.get('ReservedInstanceRenewAttribute') is not None:
            for k1 in m.get('ReservedInstanceRenewAttribute'):
                temp_model = main_models.DescribeReservedInstanceAutoRenewAttributeResponseBodyReservedInstanceRenewAttributesReservedInstanceRenewAttribute()
                self.reserved_instance_renew_attribute.append(temp_model.from_map(k1))

        return self

class DescribeReservedInstanceAutoRenewAttributeResponseBodyReservedInstanceRenewAttributesReservedInstanceRenewAttribute(DaraModel):
    def __init__(
        self,
        duration: int = None,
        period_unit: str = None,
        renewal_status: str = None,
        reserved_instance_id: str = None,
    ):
        # The auto-renewal duration.
        self.duration = duration
        # The unit of the auto-renewal duration.
        # 
        # Valid values: Year and Month.
        self.period_unit = period_unit
        # The auto-renewal status of the reserved instance. Valid values:
        # 
        # *   AutoRenewal: automatically renews the reserved instance.
        # *   Normal: manually renews the reserved instances.
        self.renewal_status = renewal_status
        # The ID of the reserved instance.
        self.reserved_instance_id = reserved_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')

        return self

