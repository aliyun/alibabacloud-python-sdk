# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneNumberAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        phone_number_attribute: main_models.DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.phone_number_attribute = phone_number_attribute
        self.request_id = request_id

    def validate(self):
        if self.phone_number_attribute:
            self.phone_number_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.phone_number_attribute is not None:
            result['PhoneNumberAttribute'] = self.phone_number_attribute.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PhoneNumberAttribute') is not None:
            temp_model = main_models.DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute()
            self.phone_number_attribute = temp_model.from_map(m.get('PhoneNumberAttribute'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute(DaraModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        city: str = None,
        is_number_portability: bool = None,
        number_segment: int = None,
        province: str = None,
    ):
        self.basic_carrier = basic_carrier
        self.carrier = carrier
        self.city = city
        self.is_number_portability = is_number_portability
        self.number_segment = number_segment
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_carrier is not None:
            result['BasicCarrier'] = self.basic_carrier

        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.city is not None:
            result['City'] = self.city

        if self.is_number_portability is not None:
            result['IsNumberPortability'] = self.is_number_portability

        if self.number_segment is not None:
            result['NumberSegment'] = self.number_segment

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('IsNumberPortability') is not None:
            self.is_number_portability = m.get('IsNumberPortability')

        if m.get('NumberSegment') is not None:
            self.number_segment = m.get('NumberSegment')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

