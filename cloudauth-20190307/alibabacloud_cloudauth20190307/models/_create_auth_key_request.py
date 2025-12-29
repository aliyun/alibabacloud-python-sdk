# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAuthKeyRequest(DaraModel):
    def __init__(
        self,
        auth_years: int = None,
        biz_type: str = None,
        test: bool = None,
        user_device_id: str = None,
    ):
        # When the Test flag is false or empty, AuthYears is required, in years, with a range of [1,100]. A value of 100 indicates permanent authorization.
        self.auth_years = auth_years
        # Business type. No more than 64 characters. Can be used to note specific business, such as different face usage scenarios of the access party or the customer identifier to be delivered. It is recommended to pass this parameter.
        self.biz_type = biz_type
        # Test flag. If true, it indicates using test authorization with a default duration of 30 days; if false, the authorization duration will be based on AuthYears.
        self.test = test
        # User device ID. No more than 64 characters. Can be used to identify a specific device, and it is suggested to use the physical number of the device. It is recommended to pass this parameter.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_years is not None:
            result['AuthYears'] = self.auth_years

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.test is not None:
            result['Test'] = self.test

        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthYears') is not None:
            self.auth_years = m.get('AuthYears')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Test') is not None:
            self.test = m.get('Test')

        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')

        return self

