# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneNumberOperatorAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.DescribePhoneNumberOperatorAttributeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **InvalidParameter**: The specified phone number is invalid or the parameter format is invalid.
        # *   **PhoneNumberNotfound**: No attribute information can be found for the specified phone number.
        # *   **isp.UNKNOWN**: An unknown exception occurred.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.DescribePhoneNumberOperatorAttributeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneNumberOperatorAttributeResponseBodyData(DaraModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        city: str = None,
        is_number_portability: bool = None,
        number_segment: int = None,
        province: str = None,
    ):
        # The basic carrier. Valid values:
        # 
        # *   **China Mobile**
        # *   **China Unicom**
        # *   **China Telecom**
        # *   **China Broadnet**
        self.basic_carrier = basic_carrier
        # The actual carrier, including the virtual network operator (VNO). If the phone number involves mobile number portability, the value of this parameter is the carrier after mobile number portability.
        self.carrier = carrier
        # The city where the phone number is registered.
        self.city = city
        # Indicates whether the phone number involves mobile number portability. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_number_portability = is_number_portability
        # The number segment to which the phone number belongs.
        self.number_segment = number_segment
        # The province where the phone number is registered.
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

