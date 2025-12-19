# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class AuthorizationServerMetadata(DaraModel):
    def __init__(
        self,
        authorization_request: main_models.AuthorizationRequest = None,
        issuer: str = None,
        pkce: main_models.PKCE = None,
        token_request: main_models.TokenReqeust = None,
    ):
        self.authorization_request = authorization_request
        self.issuer = issuer
        self.pkce = pkce
        self.token_request = token_request

    def validate(self):
        if self.authorization_request:
            self.authorization_request.validate()
        if self.pkce:
            self.pkce.validate()
        if self.token_request:
            self.token_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_request is not None:
            result['AuthorizationRequest'] = self.authorization_request.to_map()

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.pkce is not None:
            result['PKCE'] = self.pkce.to_map()

        if self.token_request is not None:
            result['TokenRequest'] = self.token_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRequest') is not None:
            temp_model = main_models.AuthorizationRequest()
            self.authorization_request = temp_model.from_map(m.get('AuthorizationRequest'))

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('PKCE') is not None:
            temp_model = main_models.PKCE()
            self.pkce = temp_model.from_map(m.get('PKCE'))

        if m.get('TokenRequest') is not None:
            temp_model = main_models.TokenReqeust()
            self.token_request = temp_model.from_map(m.get('TokenRequest'))

        return self

