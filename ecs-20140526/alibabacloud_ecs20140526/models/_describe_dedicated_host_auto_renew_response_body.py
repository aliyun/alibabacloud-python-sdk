# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostAutoRenewResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_host_renew_attributes: main_models.DescribeDedicatedHostAutoRenewResponseBodyDedicatedHostRenewAttributes = None,
        request_id: str = None,
    ):
        # The array that consists of dedicated host auto-renewal attributes.
        self.dedicated_host_renew_attributes = dedicated_host_renew_attributes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dedicated_host_renew_attributes:
            self.dedicated_host_renew_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_renew_attributes is not None:
            result['DedicatedHostRenewAttributes'] = self.dedicated_host_renew_attributes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostRenewAttributes') is not None:
            temp_model = main_models.DescribeDedicatedHostAutoRenewResponseBodyDedicatedHostRenewAttributes()
            self.dedicated_host_renew_attributes = temp_model.from_map(m.get('DedicatedHostRenewAttributes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDedicatedHostAutoRenewResponseBodyDedicatedHostRenewAttributes(DaraModel):
    def __init__(
        self,
        dedicated_host_renew_attribute: List[main_models.DescribeDedicatedHostAutoRenewResponseBodyDedicatedHostRenewAttributesDedicatedHostRenewAttribute] = None,
    ):
        self.dedicated_host_renew_attribute = dedicated_host_renew_attribute

    def validate(self):
        if self.dedicated_host_renew_attribute:
            for v1 in self.dedicated_host_renew_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedHostRenewAttribute'] = []
        if self.dedicated_host_renew_attribute is not None:
            for k1 in self.dedicated_host_renew_attribute:
                result['DedicatedHostRenewAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_renew_attribute = []
        if m.get('DedicatedHostRenewAttribute') is not None:
            for k1 in m.get('DedicatedHostRenewAttribute'):
                temp_model = main_models.DescribeDedicatedHostAutoRenewResponseBodyDedicatedHostRenewAttributesDedicatedHostRenewAttribute()
                self.dedicated_host_renew_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostAutoRenewResponseBodyDedicatedHostRenewAttributesDedicatedHostRenewAttribute(DaraModel):
    def __init__(
        self,
        auto_renew_enabled: bool = None,
        auto_renew_with_ecs: str = None,
        dedicated_host_id: str = None,
        duration: int = None,
        period_unit: str = None,
        renewal_status: str = None,
    ):
        # Indicates whether auto-renewal is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew_enabled = auto_renew_enabled
        # Indicates whether the dedicated host is automatically renewed if a subscription ECS instance it hosts, after being automatically renewed, has a new expiration time that is later than that of the dedicated host. Valid values:
        # 
        # *   AutoRenewWithEcs: The dedicated host is automatically renewed along with the ECS instance.
        # *   StopRenewWithEcs: The dedicated host is not automatically renewed along with the ECS instance.
        self.auto_renew_with_ecs = auto_renew_with_ecs
        # The ID of the dedicated host.
        self.dedicated_host_id = dedicated_host_id
        # The auto-renewal period.
        self.duration = duration
        # The unit of the auto-renewal duration. Valid values:
        # 
        # *   Week
        # *   Month
        self.period_unit = period_unit
        # Indicates whether the subscription dedicated host is automatically renewed. Valid values:
        # 
        # *   AutoRenewal: The dedicated host is automatically renewed.
        # *   Normal: The dedicated host is not automatically renewed, but renewal notifications are sent.
        # *   NotRenewal: The dedicated host is not automatically renewed, and no expiration notification is sent. Alibaba Cloud sends only a non-renewal notice three days before the host expires. If the renewal status of a dedicated host is NotRenewal, you can change the value to Normal and then call [RenewDedicatedHosts](https://help.aliyun.com/document_detail/93287.html) to manually renew the dedicated host, or directly change the value to AutoRenewal.
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_enabled is not None:
            result['AutoRenewEnabled'] = self.auto_renew_enabled

        if self.auto_renew_with_ecs is not None:
            result['AutoRenewWithEcs'] = self.auto_renew_with_ecs

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')

        if m.get('AutoRenewWithEcs') is not None:
            self.auto_renew_with_ecs = m.get('AutoRenewWithEcs')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        return self

