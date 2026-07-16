# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthorizationServerDescriptionRequest(DaraModel):
    def __init__(
        self,
        authorization_server_id: str = None,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # The authorization server ID.
        # 
        # This parameter is required.
        self.authorization_server_id = authorization_server_id
        # The client token that is used to ensure the idempotence of the request. Generate a parameter value from your client to ensure that the value is unique among different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, refer to References: [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the authorization server.
        self.description = description
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
        if self.authorization_server_id is not None:
            result['AuthorizationServerId'] = self.authorization_server_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationServerId') is not None:
            self.authorization_server_id = m.get('AuthorizationServerId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

