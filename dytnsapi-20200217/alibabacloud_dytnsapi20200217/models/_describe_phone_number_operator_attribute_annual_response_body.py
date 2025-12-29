# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneNumberOperatorAttributeAnnualResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribePhoneNumberOperatorAttributeAnnualResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribePhoneNumberOperatorAttributeAnnualResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribePhoneNumberOperatorAttributeAnnualResponseBodyData(DaraModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        city: str = None,
        mts: str = None,
        number_portability: bool = None,
        province: str = None,
    ):
        self.basic_carrier = basic_carrier
        self.carrier = carrier
        self.city = city
        self.mts = mts
        self.number_portability = number_portability
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

        if self.mts is not None:
            result['Mts'] = self.mts

        if self.number_portability is not None:
            result['NumberPortability'] = self.number_portability

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

        if m.get('Mts') is not None:
            self.mts = m.get('Mts')

        if m.get('NumberPortability') is not None:
            self.number_portability = m.get('NumberPortability')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

