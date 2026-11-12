# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LoginInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
        port: int = None,
        region_id: str = None,
        username: str = None,
    ):
        # The instance ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The password associated with the username of the simple application server.
        # 
        # - Linux server: No password is required.
        # - Windows server: Enter the configured password. If you have not set a password after purchasing the simple application server, see [Reset the password](https://help.aliyun.com/document_detail/60055.html).
        self.password = password
        # The port number for remote logon to the instance.
        # 
        # - Linux server: The default port is 22.
        # 
        # - Windows server: The default port is 3389.
        # 
        # > If you want to connect to the server by using a custom port, you must first change the default remote port of the server. For more information, see [Settings for custom remote connection ports](https://help.aliyun.com/document_detail/2807402.html).
        self.port = port
        # The region ID of the specified Simple Application Server instance. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The username for the simple application server.
        # 
        # - You do not need to enter a username for a Linux server.
        # - The default username for a Windows server is `administrator`.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

