# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCustomAuthIdentityRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        instance_id: str = None,
        next_token: str = None,
        size: int = None,
        username: str = None,
    ):
        # The client ID of the device. You can specify this parameter when the identity type is CLIENT.
        self.client_id = client_id
        # The identity type.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end position of the current query. You can pass this token as a parameter in the next call to continue paginating. If this is the first call or the last page is returned, the value is an empty string.
        self.next_token = next_token
        # The number of entries to query. Maximum value: 100.
        # 
        # This parameter is required.
        self.size = size
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.size is not None:
            result['Size'] = self.size

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

