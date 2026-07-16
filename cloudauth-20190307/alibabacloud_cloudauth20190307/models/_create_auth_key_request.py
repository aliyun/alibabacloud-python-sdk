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
        # The authorization duration. This parameter is required when the Test parameter is set to false or is left empty. Unit: years. Valid values: 1 to 100. A value of 100 indicates permanent authorization.
        self.auth_years = auth_years
        # The business type. The value can be up to 64 characters in length. You can use this parameter to add remarks for a specific business, such as different facial recognition scenarios of the requester or the customer identifier to be delivered. We recommend that you specify this parameter.
        self.biz_type = biz_type
        # The test identifier. Valid values:
        # - true: Uses test authorization. The authorization duration is 30 days by default.
        # - false: The authorization duration is determined by the AuthYears parameter.
        self.test = test
        # The user device ID. The value can be up to 64 characters in length. You can use this parameter to identify a specific device. We recommend that you use the physical device number. We recommend that you specify this parameter.
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

