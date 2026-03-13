# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GenerateWebAuthnAuthenticatorRegistrationUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        web_authn_authenticator_registration_url: main_models.GenerateWebAuthnAuthenticatorRegistrationUrlResponseBodyWebAuthnAuthenticatorRegistrationUrl = None,
    ):
        self.request_id = request_id
        self.web_authn_authenticator_registration_url = web_authn_authenticator_registration_url

    def validate(self):
        if self.web_authn_authenticator_registration_url:
            self.web_authn_authenticator_registration_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.web_authn_authenticator_registration_url is not None:
            result['WebAuthnAuthenticatorRegistrationUrl'] = self.web_authn_authenticator_registration_url.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WebAuthnAuthenticatorRegistrationUrl') is not None:
            temp_model = main_models.GenerateWebAuthnAuthenticatorRegistrationUrlResponseBodyWebAuthnAuthenticatorRegistrationUrl()
            self.web_authn_authenticator_registration_url = temp_model.from_map(m.get('WebAuthnAuthenticatorRegistrationUrl'))

        return self

class GenerateWebAuthnAuthenticatorRegistrationUrlResponseBodyWebAuthnAuthenticatorRegistrationUrl(DaraModel):
    def __init__(
        self,
        registration_url: str = None,
        registration_url_parameters: str = None,
    ):
        # 注册WebAuthn认证器URL
        self.registration_url = registration_url
        # 注册WebAuthn认证器URL参数
        self.registration_url_parameters = registration_url_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registration_url is not None:
            result['RegistrationUrl'] = self.registration_url

        if self.registration_url_parameters is not None:
            result['RegistrationUrlParameters'] = self.registration_url_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrationUrl') is not None:
            self.registration_url = m.get('RegistrationUrl')

        if m.get('RegistrationUrlParameters') is not None:
            self.registration_url_parameters = m.get('RegistrationUrlParameters')

        return self

