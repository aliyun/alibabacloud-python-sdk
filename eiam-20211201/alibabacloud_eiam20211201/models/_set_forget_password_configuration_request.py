# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetForgetPasswordConfigurationRequest(DaraModel):
    def __init__(
        self,
        authentication_channels: List[str] = None,
        forget_password_status: str = None,
        instance_id: str = None,
    ):
        # The authentication channels. Valid values: email and sms.
        self.authentication_channels = authentication_channels
        # The status of the forgot password feature. Valid values: enabled and disabled.
        # 
        # This parameter is required.
        self.forget_password_status = forget_password_status
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_channels is not None:
            result['AuthenticationChannels'] = self.authentication_channels

        if self.forget_password_status is not None:
            result['ForgetPasswordStatus'] = self.forget_password_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationChannels') is not None:
            self.authentication_channels = m.get('AuthenticationChannels')

        if m.get('ForgetPasswordStatus') is not None:
            self.forget_password_status = m.get('ForgetPasswordStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

