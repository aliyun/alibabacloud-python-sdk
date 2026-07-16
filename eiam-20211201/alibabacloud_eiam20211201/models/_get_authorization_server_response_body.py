# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetAuthorizationServerResponseBody(DaraModel):
    def __init__(
        self,
        authorization_server: main_models.GetAuthorizationServerResponseBodyAuthorizationServer = None,
        request_id: str = None,
    ):
        # The authorization server.
        self.authorization_server = authorization_server
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.authorization_server:
            self.authorization_server.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_server is not None:
            result['AuthorizationServer'] = self.authorization_server.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationServer') is not None:
            temp_model = main_models.GetAuthorizationServerResponseBodyAuthorizationServer()
            self.authorization_server = temp_model.from_map(m.get('AuthorizationServer'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAuthorizationServerResponseBodyAuthorizationServer(DaraModel):
    def __init__(
        self,
        authorization_server_id: str = None,
        authorization_server_name: str = None,
        create_time: int = None,
        creation_type: str = None,
        description: str = None,
        instance_id: str = None,
        issuer: str = None,
        issuer_domain: str = None,
        issuer_mode: str = None,
        last_update_time: int = None,
        protocol_endpoint: main_models.GetAuthorizationServerResponseBodyAuthorizationServerProtocolEndpoint = None,
        status: str = None,
    ):
        # The authorization server ID.
        self.authorization_server_id = authorization_server_id
        # The name of the authorization server.
        self.authorization_server_name = authorization_server_name
        # The time when the authorization server was created.
        self.create_time = create_time
        # The creation type.
        self.creation_type = creation_type
        # The description of the authorization server.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The issuer of the authorization token.
        self.issuer = issuer
        # The domain name used by the issuer.
        self.issuer_domain = issuer_domain
        # The issuer mode.
        self.issuer_mode = issuer_mode
        # The time when the authorization server was last updated.
        self.last_update_time = last_update_time
        # The endpoint configuration of the authorization server.
        self.protocol_endpoint = protocol_endpoint
        # The status of the authorization server.
        self.status = status

    def validate(self):
        if self.protocol_endpoint:
            self.protocol_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_server_id is not None:
            result['AuthorizationServerId'] = self.authorization_server_id

        if self.authorization_server_name is not None:
            result['AuthorizationServerName'] = self.authorization_server_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.issuer_domain is not None:
            result['IssuerDomain'] = self.issuer_domain

        if self.issuer_mode is not None:
            result['IssuerMode'] = self.issuer_mode

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.protocol_endpoint is not None:
            result['ProtocolEndpoint'] = self.protocol_endpoint.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationServerId') is not None:
            self.authorization_server_id = m.get('AuthorizationServerId')

        if m.get('AuthorizationServerName') is not None:
            self.authorization_server_name = m.get('AuthorizationServerName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('IssuerDomain') is not None:
            self.issuer_domain = m.get('IssuerDomain')

        if m.get('IssuerMode') is not None:
            self.issuer_mode = m.get('IssuerMode')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('ProtocolEndpoint') is not None:
            temp_model = main_models.GetAuthorizationServerResponseBodyAuthorizationServerProtocolEndpoint()
            self.protocol_endpoint = temp_model.from_map(m.get('ProtocolEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetAuthorizationServerResponseBodyAuthorizationServerProtocolEndpoint(DaraModel):
    def __init__(
        self,
        oauth_2token_endpoint: str = None,
        oidc_jwks_endpoint: str = None,
    ):
        # The token endpoint of the authorization server.
        self.oauth_2token_endpoint = oauth_2token_endpoint
        # The JWKS endpoint of the authorization server.
        self.oidc_jwks_endpoint = oidc_jwks_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oauth_2token_endpoint is not None:
            result['Oauth2TokenEndpoint'] = self.oauth_2token_endpoint

        if self.oidc_jwks_endpoint is not None:
            result['OidcJwksEndpoint'] = self.oidc_jwks_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oauth2TokenEndpoint') is not None:
            self.oauth_2token_endpoint = m.get('Oauth2TokenEndpoint')

        if m.get('OidcJwksEndpoint') is not None:
            self.oidc_jwks_endpoint = m.get('OidcJwksEndpoint')

        return self

