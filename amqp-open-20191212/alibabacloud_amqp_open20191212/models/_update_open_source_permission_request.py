# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOpenSourcePermissionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        configure: str = None,
        instance_id: str = None,
        read: str = None,
        user_name: str = None,
        vhost: str = None,
        write: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The regular expression for configure permissions.
        self.configure = configure
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The regular expression for read permissions.
        self.read = read
        # The username.
        self.user_name = user_name
        # The vhost name.
        self.vhost = vhost
        # The regular expression for write permissions.
        self.write = write

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.configure is not None:
            result['Configure'] = self.configure

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.read is not None:
            result['Read'] = self.read

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vhost is not None:
            result['Vhost'] = self.vhost

        if self.write is not None:
            result['Write'] = self.write

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Configure') is not None:
            self.configure = m.get('Configure')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Read') is not None:
            self.read = m.get('Read')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        if m.get('Write') is not None:
            self.write = m.get('Write')

        return self

