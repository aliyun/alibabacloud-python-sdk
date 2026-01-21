# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ReplaceServersInServerGroupRequest(DaraModel):
    def __init__(
        self,
        added_servers: List[main_models.ReplaceServersInServerGroupRequestAddedServers] = None,
        client_token: str = None,
        dry_run: bool = None,
        removed_servers: List[main_models.ReplaceServersInServerGroupRequestRemovedServers] = None,
        server_group_id: str = None,
    ):
        # This parameter is required.
        self.added_servers = added_servers
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a `2xx` HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The backend servers that you want to remove.
        # 
        # This parameter is required.
        self.removed_servers = removed_servers
        # The ID of the server group.
        # 
        # > You cannot perform this operation on a server group of the Function type.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id

    def validate(self):
        if self.added_servers:
            for v1 in self.added_servers:
                 if v1:
                    v1.validate()
        if self.removed_servers:
            for v1 in self.removed_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddedServers'] = []
        if self.added_servers is not None:
            for k1 in self.added_servers:
                result['AddedServers'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['RemovedServers'] = []
        if self.removed_servers is not None:
            for k1 in self.removed_servers:
                result['RemovedServers'].append(k1.to_map() if k1 else None)

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.added_servers = []
        if m.get('AddedServers') is not None:
            for k1 in m.get('AddedServers'):
                temp_model = main_models.ReplaceServersInServerGroupRequestAddedServers()
                self.added_servers.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.removed_servers = []
        if m.get('RemovedServers') is not None:
            for k1 in m.get('RemovedServers'):
                temp_model = main_models.ReplaceServersInServerGroupRequestRemovedServers()
                self.removed_servers.append(temp_model.from_map(k1))

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        return self

class ReplaceServersInServerGroupRequestRemovedServers(DaraModel):
    def __init__(
        self,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
    ):
        # The port that is used by the backend server. Valid values: **1** to **65535**. You can specify at most 200 servers in each call.
        self.port = port
        # The ID of the backend server. You can specify at most 200 servers in each call.
        # 
        # *   If the server group is of the **Instance** type, set ServerId to the ID of a resource of the **Ecs**, **Eni**, or **Eci** type.
        # *   If the server group is of the **Ip** type, set ServerId to IP addresses.
        # 
        # >  You cannot perform this operation on a server group of the Function Compute type. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the type of server groups.
        # 
        # This parameter is required.
        self.server_id = server_id
        # The IP address of the ENI in exclusive mode.
        self.server_ip = server_ip
        # The type of backend server. You can specify at most 200 servers in each call. Valid values:
        # 
        # *   **Ecs**: ECS instance
        # *   **Eni**: ENI
        # *   **Eci**: elastic container instance
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        return self

class ReplaceServersInServerGroupRequestAddedServers(DaraModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        self.description = description
        self.port = port
        self.server_id = server_id
        self.server_ip = server_ip
        self.server_type = server_type
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

