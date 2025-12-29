# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribeMobileOperatorAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.DescribeMobileOperatorAttributeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeMobileOperatorAttributeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMobileOperatorAttributeResponseBodyData(DaraModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        city: str = None,
        is_number_portability: bool = None,
        province: str = None,
        real_number: str = None,
        segment_carrier: str = None,
    ):
        self.basic_carrier = basic_carrier
        self.carrier = carrier
        self.city = city
        self.is_number_portability = is_number_portability
        self.province = province
        self.real_number = real_number
        self.segment_carrier = segment_carrier

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

        if self.province is not None:
            result['Province'] = self.province

        if self.real_number is not None:
            result['RealNumber'] = self.real_number

        if self.segment_carrier is not None:
            result['SegmentCarrier'] = self.segment_carrier

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

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')

        if m.get('SegmentCarrier') is not None:
            self.segment_carrier = m.get('SegmentCarrier')

        return self

