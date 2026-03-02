# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetVerificationInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_email_device: main_models.GetVerificationInfoResponseBodySecurityEmailDevice = None,
        security_phone_device: main_models.GetVerificationInfoResponseBodySecurityPhoneDevice = None,
    ):
        self.request_id = request_id
        self.security_email_device = security_email_device
        self.security_phone_device = security_phone_device

    def validate(self):
        if self.security_email_device:
            self.security_email_device.validate()
        if self.security_phone_device:
            self.security_phone_device.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_email_device is not None:
            result['SecurityEmailDevice'] = self.security_email_device.to_map()

        if self.security_phone_device is not None:
            result['SecurityPhoneDevice'] = self.security_phone_device.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEmailDevice') is not None:
            temp_model = main_models.GetVerificationInfoResponseBodySecurityEmailDevice()
            self.security_email_device = temp_model.from_map(m.get('SecurityEmailDevice'))

        if m.get('SecurityPhoneDevice') is not None:
            temp_model = main_models.GetVerificationInfoResponseBodySecurityPhoneDevice()
            self.security_phone_device = temp_model.from_map(m.get('SecurityPhoneDevice'))

        return self

class GetVerificationInfoResponseBodySecurityPhoneDevice(DaraModel):
    def __init__(
        self,
        area_code: str = None,
        phone_number: str = None,
        status: str = None,
    ):
        self.area_code = area_code
        self.phone_number = phone_number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetVerificationInfoResponseBodySecurityEmailDevice(DaraModel):
    def __init__(
        self,
        email: str = None,
        status: str = None,
    ):
        self.email = email
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

