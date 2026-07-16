# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class AddServersToServerGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        server_group_id: str = None,
        servers: List[main_models.AddServersToServerGroupRequestServers] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: prechecks the request, but does not add a backend server to a server group. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The server group ID.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The backend servers. You can specify at most 200 servers in each call.
        # 
        # This parameter is required.
        self.servers = servers

    def validate(self):
        if self.servers:
            for v1 in self.servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        result['Servers'] = []
        if self.servers is not None:
            for k1 in self.servers:
                result['Servers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        self.servers = []
        if m.get('Servers') is not None:
            for k1 in m.get('Servers'):
                temp_model = main_models.AddServersToServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k1))

        return self

class AddServersToServerGroupRequestServers(DaraModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        remote_ip_enabled: bool = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # The description of the backend server. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The port that is used by the backend server. Valid values: **1** to **65535**. You can specify at most 200 servers in each call.
        # 
        # >  This parameter is required if you set **ServerType** to **Ecs**, **Eni**, **Eci**, or **Ip**. You do not need to set this parameter if **ServerType** is set to **Fc**.
        self.port = port
        # Specifies whether to enable the remote IP feature. You can specify at most 200 servers in each call. Default values:
        # 
        # *   **true**: enables the feature.
        # *   **false**: disables the feature.
        # 
        # >  This parameter takes effect only when **ServerType** is set to **Ip**.
        self.remote_ip_enabled = remote_ip_enabled
        # The ID of the server group. You can specify at most 200 servers in each call.
        # 
        # *   If the server group is of the **Instance** type, set ServerId to the ID of a resource of the **Ecs**, **Eni**, or **Eci** type.
        # *   If the server group is of the **Ip** type, set this parameter to IP addresses.
        # *   If the server group is of the **Fc** type, set ServerId to an Alibaba Cloud Resource Name (ARN).
        self.server_id = server_id
        # The IP address of the backend server. You can specify at most 200 servers in each call.
        # 
        # >  You do not need to set this parameter if you set **ServerType** to **Fc**.
        self.server_ip = server_ip
        # The type of the backend server. You can specify at most 200 servers in each call. Default values:
        # 
        # *   **Ecs**: Elastic Compute Service (ECS) instance
        # *   **Eni**: elastic network interface (ENI)
        # *   **Eci**: elastic container instance
        # *   **Ip**: IP address
        # *   **Fc**: Function Compute
        # 
        # This parameter is required.
        self.server_type = server_type
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the value is set to **0**, no requests are forwarded to the server. You can specify at most 200 servers in each call.
        # 
        # >  You do not need to set this parameter if you set **ServerType** to **Fc**.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.port is not None:
            result['Port'] = self.port

        if self.remote_ip_enabled is not None:
            result['RemoteIpEnabled'] = self.remote_ip_enabled

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RemoteIpEnabled') is not None:
            self.remote_ip_enabled = m.get('RemoteIpEnabled')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

