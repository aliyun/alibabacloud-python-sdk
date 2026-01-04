# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetForgetPasswordConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        open_forget_password_configuration: main_models.GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration = None,
        request_id: str = None,
    ):
        # The forgot password configurations.
        self.open_forget_password_configuration = open_forget_password_configuration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.open_forget_password_configuration:
            self.open_forget_password_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_forget_password_configuration is not None:
            result['OpenForgetPasswordConfiguration'] = self.open_forget_password_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenForgetPasswordConfiguration') is not None:
            temp_model = main_models.GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration()
            self.open_forget_password_configuration = temp_model.from_map(m.get('OpenForgetPasswordConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration(DaraModel):
    def __init__(
        self,
        authentication_channels: List[str] = None,
        enable: bool = None,
        enable_email: bool = None,
        enable_sms: bool = None,
        forget_password_status: str = None,
    ):
        # The authentication channels. Valid values:  
        # email  
        # sms  
        # totp  
        # web_authn
        self.authentication_channels = authentication_channels
        # Indicates whether the forgot password feature is enabled.
        self.enable = enable
        # Indicates whether email authentication is enabled for the forgot password feature.
        self.enable_email = enable_email
        # Indicates whether Short Message Service (SMS) authentication is enabled for the forgot password feature.
        self.enable_sms = enable_sms
        # The status of the forgot password feature. Valid values: enabled and disabled.
        self.forget_password_status = forget_password_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_channels is not None:
            result['AuthenticationChannels'] = self.authentication_channels

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.enable_email is not None:
            result['EnableEmail'] = self.enable_email

        if self.enable_sms is not None:
            result['EnableSms'] = self.enable_sms

        if self.forget_password_status is not None:
            result['ForgetPasswordStatus'] = self.forget_password_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationChannels') is not None:
            self.authentication_channels = m.get('AuthenticationChannels')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnableEmail') is not None:
            self.enable_email = m.get('EnableEmail')

        if m.get('EnableSms') is not None:
            self.enable_sms = m.get('EnableSms')

        if m.get('ForgetPasswordStatus') is not None:
            self.forget_password_status = m.get('ForgetPasswordStatus')

        return self

