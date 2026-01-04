# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        instance_renew_attributes: main_models.DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes = None,
        request_id: str = None,
    ):
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The renewal status of the instance.
        self.instance_renew_attributes = instance_renew_attributes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_renew_attributes:
            self.instance_renew_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_renew_attributes is not None:
            result['InstanceRenewAttributes'] = self.instance_renew_attributes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceRenewAttributes') is not None:
            temp_model = main_models.DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes()
            self.instance_renew_attributes = temp_model.from_map(m.get('InstanceRenewAttributes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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
        auto_renewal: bool = None,
        duration: str = None,
        instance_id: str = None,
    ):
        # The renewal type of the instance.
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal.
        self.auto_renewal = auto_renewal
        # The unit of the auto-renewal period.
        self.duration = duration
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

