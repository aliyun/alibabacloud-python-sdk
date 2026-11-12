# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        instance_name: str = None,
        password: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **ClientToken** parameter supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The instance ID of the Simple Application Server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the server. The name must be 2 to 50 characters in length, and must start with a letter, digit, or Chinese character. It can contain digits, underscores (_), and hyphens (-). Domain names are also supported.
        self.instance_name = instance_name
        # The new password of the server. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include:
        # 
        # ```
        # ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # ```
        # 
        # The password of a Windows instance cannot start with a forward slash (/).
        # 
        # > If you specify the `Password` parameter, send the request over HTTPS to prevent password leaks.
        self.password = password
        # The region ID of the Simple Application Server.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

