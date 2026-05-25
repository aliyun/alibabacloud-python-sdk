# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20230101 import models as main_models
from darabonba.model import DaraModel

class DescribeNumberHLRResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.DescribeNumberHLRResponseBodyData = None,
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
            temp_model = main_models.DescribeNumberHLRResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNumberHLRResponseBodyData(DaraModel):
    def __init__(
        self,
        blocked: str = None,
        call: main_models.DescribeNumberHLRResponseBodyDataCall = None,
        carrier: str = None,
        city: str = None,
        country_iso_3: str = None,
        live: main_models.DescribeNumberHLRResponseBodyDataLive = None,
        phone_type: str = None,
        sms: main_models.DescribeNumberHLRResponseBodyDataSms = None,
    ):
        self.blocked = blocked
        self.call = call
        self.carrier = carrier
        self.city = city
        self.country_iso_3 = country_iso_3
        self.live = live
        self.phone_type = phone_type
        self.sms = sms

    def validate(self):
        if self.call:
            self.call.validate()
        if self.live:
            self.live.validate()
        if self.sms:
            self.sms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blocked is not None:
            result['Blocked'] = self.blocked

        if self.call is not None:
            result['Call'] = self.call.to_map()

        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.city is not None:
            result['City'] = self.city

        if self.country_iso_3 is not None:
            result['CountryIso3'] = self.country_iso_3

        if self.live is not None:
            result['Live'] = self.live.to_map()

        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type

        if self.sms is not None:
            result['Sms'] = self.sms.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blocked') is not None:
            self.blocked = m.get('Blocked')

        if m.get('Call') is not None:
            temp_model = main_models.DescribeNumberHLRResponseBodyDataCall()
            self.call = temp_model.from_map(m.get('Call'))

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CountryIso3') is not None:
            self.country_iso_3 = m.get('CountryIso3')

        if m.get('Live') is not None:
            temp_model = main_models.DescribeNumberHLRResponseBodyDataLive()
            self.live = temp_model.from_map(m.get('Live'))

        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')

        if m.get('Sms') is not None:
            temp_model = main_models.DescribeNumberHLRResponseBodyDataSms()
            self.sms = temp_model.from_map(m.get('Sms'))

        return self

class DescribeNumberHLRResponseBodyDataSms(DaraModel):
    def __init__(
        self,
        cleansed_code: int = None,
        max_length: int = None,
        min_length: int = None,
    ):
        # sms
        self.cleansed_code = cleansed_code
        self.max_length = max_length
        self.min_length = min_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cleansed_code is not None:
            result['CleansedCode'] = self.cleansed_code

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleansedCode') is not None:
            self.cleansed_code = m.get('CleansedCode')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        return self

class DescribeNumberHLRResponseBodyDataLive(DaraModel):
    def __init__(
        self,
        device_status: str = None,
        roaming: str = None,
        roaming_country: str = None,
        subscriber_status: str = None,
    ):
        self.device_status = device_status
        self.roaming = roaming
        self.roaming_country = roaming_country
        self.subscriber_status = subscriber_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.roaming is not None:
            result['Roaming'] = self.roaming

        if self.roaming_country is not None:
            result['RoamingCountry'] = self.roaming_country

        if self.subscriber_status is not None:
            result['SubscriberStatus'] = self.subscriber_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('Roaming') is not None:
            self.roaming = m.get('Roaming')

        if m.get('RoamingCountry') is not None:
            self.roaming_country = m.get('RoamingCountry')

        if m.get('SubscriberStatus') is not None:
            self.subscriber_status = m.get('SubscriberStatus')

        return self



class DescribeNumberHLRResponseBodyDataCall(DaraModel):
    def __init__(
        self,
        cleansed_code: str = None,
        max_length: int = None,
        min_length: int = None,
    ):
        # call
        self.cleansed_code = cleansed_code
        self.max_length = max_length
        self.min_length = min_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cleansed_code is not None:
            result['CleansedCode'] = self.cleansed_code

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleansedCode') is not None:
            self.cleansed_code = m.get('CleansedCode')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        return self

