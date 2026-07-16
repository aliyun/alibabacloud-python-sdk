# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthorizationServerRequest(DaraModel):
    def __init__(
        self,
        authorization_server_id: str = None,
        authorization_server_name: str = None,
        client_token: str = None,
        instance_id: str = None,
        issuer_domain: str = None,
        issuer_mode: str = None,
    ):
        # The authorization server ID.
        # 
        # This parameter is required.
        self.authorization_server_id = authorization_server_id
        # The name of the authorization server.
        self.authorization_server_name = authorization_server_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate a parameter value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see References: [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The domain name used by the issuer.
        self.issuer_domain = issuer_domain
        # The issuer mode.
        self.issuer_mode = issuer_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_server_id is not None:
            result['AuthorizationServerId'] = self.authorization_server_id

        if self.authorization_server_name is not None:
            result['AuthorizationServerName'] = self.authorization_server_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer_domain is not None:
            result['IssuerDomain'] = self.issuer_domain

        if self.issuer_mode is not None:
            result['IssuerMode'] = self.issuer_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationServerId') is not None:
            self.authorization_server_id = m.get('AuthorizationServerId')

        if m.get('AuthorizationServerName') is not None:
            self.authorization_server_name = m.get('AuthorizationServerName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IssuerDomain') is not None:
            self.issuer_domain = m.get('IssuerDomain')

        if m.get('IssuerMode') is not None:
            self.issuer_mode = m.get('IssuerMode')

        return self

