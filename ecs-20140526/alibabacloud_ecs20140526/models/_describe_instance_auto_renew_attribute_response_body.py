# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        instance_renew_attributes: main_models.DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The renewal attributes of instances.
        self.instance_renew_attributes = instance_renew_attributes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of queried instances.
        self.total_count = total_count

    def validate(self):
        if self.instance_renew_attributes:
            self.instance_renew_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_renew_attributes is not None:
            result['InstanceRenewAttributes'] = self.instance_renew_attributes.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceRenewAttributes') is not None:
            temp_model = main_models.DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes()
            self.instance_renew_attributes = temp_model.from_map(m.get('InstanceRenewAttributes'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes(DaraModel):
    def __init__(
        self,
        instance_renew_attribute: List[main_models.DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute] = None,
    ):
        self.instance_renew_attribute = instance_renew_attribute

    def validate(self):
        if self.instance_renew_attribute:
            for v1 in self.instance_renew_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRenewAttribute'] = []
        if self.instance_renew_attribute is not None:
            for k1 in self.instance_renew_attribute:
                result['InstanceRenewAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_renew_attribute = []
        if m.get('InstanceRenewAttribute') is not None:
            for k1 in m.get('InstanceRenewAttribute'):
                temp_model = main_models.DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute()
                self.instance_renew_attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute(DaraModel):
    def __init__(
        self,
        auto_renew_enabled: bool = None,
        duration: int = None,
        enable_expected_renew_day: bool = None,
        instance_id: str = None,
        period_unit: str = None,
        renewal_status: str = None,
    ):
        # Indicates whether auto-renewal is enabled.
        self.auto_renew_enabled = auto_renew_enabled
        # The auto-renewal duration.
        self.duration = duration
        self.enable_expected_renew_day = enable_expected_renew_day
        # The ID of the instance.
        self.instance_id = instance_id
        # The unit of the auto-renewal duration.
        self.period_unit = period_unit
        # The auto-renewal state of the instance. Valid values:
        # 
        # *   AutoRenewal: Auto-renewal is enabled for the instance.
        # *   Normal: Auto-renewal is disabled for the instance.
        # *   NotRenewal: The instance is not to be renewed. The system sends no more expiration reminders, but sends only a non-renewal reminder three days before the expiration date. For an instance that is not to be renewed, you can call the [ModifyInstanceAutoRenewAttribute](https://help.aliyun.com/document_detail/52843.html) operation to change its auto-renewal status to `Normal`. Then, you can manually renew the instance or enable auto-renewal for the instance.
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

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable_expected_renew_day is not None:
            result['EnableExpectedRenewDay'] = self.enable_expected_renew_day

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EnableExpectedRenewDay') is not None:
            self.enable_expected_renew_day = m.get('EnableExpectedRenewDay')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        return self

