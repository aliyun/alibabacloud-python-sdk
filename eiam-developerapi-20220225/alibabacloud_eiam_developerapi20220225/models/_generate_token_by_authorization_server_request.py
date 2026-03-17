# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTokenByAuthorizationServerRequest(DaraModel):
    def __init__(
        self,
        application_federated_credential_name: str = None,
        client_assertion: str = None,
        client_assertion_type: str = None,
        client_id: str = None,
        client_secret: str = None,
        client_x509: str = None,
        client_x509chain: str = None,
        code: str = None,
        code_verifier: str = None,
        device_code: str = None,
        grant_type: str = None,
        password: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
        scope: str = None,
        username: str = None,
    ):
        self.application_federated_credential_name = application_federated_credential_name
        self.client_assertion = client_assertion
        self.client_assertion_type = client_assertion_type
        # This parameter is required.
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_x509 = client_x509
        self.client_x509chain = client_x509chain
        self.code = code
        self.code_verifier = code_verifier
        self.device_code = device_code
        # This parameter is required.
        self.grant_type = grant_type
        self.password = password
        self.redirect_uri = redirect_uri
        self.refresh_token = refresh_token
        self.scope = scope
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_federated_credential_name is not None:
            result['application_federated_credential_name'] = self.application_federated_credential_name

        if self.client_assertion is not None:
            result['client_assertion'] = self.client_assertion

        if self.client_assertion_type is not None:
            result['client_assertion_type'] = self.client_assertion_type

        if self.client_id is not None:
            result['client_id'] = self.client_id

        if self.client_secret is not None:
            result['client_secret'] = self.client_secret

        if self.client_x509 is not None:
            result['client_x509'] = self.client_x509

        if self.client_x509chain is not None:
            result['client_x509_chain'] = self.client_x509chain

        if self.code is not None:
            result['code'] = self.code

        if self.code_verifier is not None:
            result['code_verifier'] = self.code_verifier

        if self.device_code is not None:
            result['device_code'] = self.device_code

        if self.grant_type is not None:
            result['grant_type'] = self.grant_type

        if self.password is not None:
            result['password'] = self.password

        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri

        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token

        if self.scope is not None:
            result['scope'] = self.scope

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application_federated_credential_name') is not None:
            self.application_federated_credential_name = m.get('application_federated_credential_name')

        if m.get('client_assertion') is not None:
            self.client_assertion = m.get('client_assertion')

        if m.get('client_assertion_type') is not None:
            self.client_assertion_type = m.get('client_assertion_type')

        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')

        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')

        if m.get('client_x509') is not None:
            self.client_x509 = m.get('client_x509')

        if m.get('client_x509_chain') is not None:
            self.client_x509chain = m.get('client_x509_chain')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('code_verifier') is not None:
            self.code_verifier = m.get('code_verifier')

        if m.get('device_code') is not None:
            self.device_code = m.get('device_code')

        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')

        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

