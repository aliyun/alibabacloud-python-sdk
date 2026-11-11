# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class AddServersToServerGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        server_group_id: str = None,
        servers: List[main_models.AddServersToServerGroupRequestServers] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without adding the servers. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the precheck, an error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query region IDs.
        self.region_id = region_id
        # The ID of the server group.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The list of backend servers.
        # 
        # > You can specify up to 200 servers in a single call.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # The description of the server.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, Chinese characters, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.description = description
        # The port used by the backend server. Valid values: **0** to **65535**. If you do not specify this parameter, the default value **0** is used.
        # 
        # If the all-port forwarding feature is enabled for the server group, you do not need to specify a port when you add a backend server. In this case, the default value 0 is used, and NLB forwards traffic to the backend server based on the frontend request port. You can check whether the all-port forwarding feature is enabled by querying the **AnyPortEnabled** field returned by the [ListServerGroups](https://help.aliyun.com/document_detail/445895.html) operation.
        self.port = port
        # The ID of the backend server.
        # 
        # - If the server group is of the **Instance** type, this parameter specifies the resource ID of an **Ecs**, **Eni**, or **Eci** resource.
        # 
        # - If the server group is of the **Ip** type, this parameter specifies an IP address.
        # 
        # This parameter is required.
        self.server_id = server_id
        # The IP address of the server. This parameter is required when the server group is of the **Ip** type.
        self.server_ip = server_ip
        # The backend server type. Valid values:
        # 
        # - **Ecs**: an ECS instance.
        # - **Eni**: an elastic network interface (ENI).
        # - **Eci**: an Elastic Container Instance (ECI).
        # - **Ip**: an IP address.
        # 
        # This parameter is required.
        self.server_type = server_type
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the weight is set to **0**, no requests are forwarded to the backend server.
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

