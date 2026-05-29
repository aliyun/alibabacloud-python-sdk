# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateServerGroupServersAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        server_group_id: str = None,
        servers: List[main_models.UpdateServerGroupServersAttributeRequestServers] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The server group ID.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The server groups. You can specify at most 40 server groups in each call.
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
                temp_model = main_models.UpdateServerGroupServersAttributeRequestServers()
                self.servers.append(temp_model.from_map(k1))

        return self

class UpdateServerGroupServersAttributeRequestServers(DaraModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # The description of the backend server. The description must be 2 to 256 characters in length, and cannot start with http:// or https://.
        self.description = description
        # The port that is used by the backend server. Valid values: **1** to **65535**.
        # 
        # > You do not need to set this parameter if **ServerType** is set to **Fc**.
        self.port = port
        # The ID of the backend server.
        # 
        # *   Specify the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance if you set **ServerType** to **Ecs**, **Eni**, or **Eci**.
        # *   Specify an IP address if you set **ServerType** to **Ip**.
        # *   Specify the Alibaba Cloud Resource Name (ARN) of a Function Compute function if you set **ServerType** to **Fc**.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: ECS instance
        # *   **Eni**: ENI
        # *   **Eci**: elastic container instance
        # *   **Ip**: IP address
        # *   **Fc**: Function Compute
        # 
        # This parameter is required.
        self.server_type = server_type
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the value is set to **0**, no requests are forwarded to the server. You can specify up to 40 servers in each call.
        # 
        # > You do not need to set this parameter if **ServerType** is set to **Fc**.
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

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

