# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListServerGroupServersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        servers: List[main_models.ListServerGroupServersResponseBodyServers] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If **NextToken** is not empty, the value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # A list of backend servers.
        self.servers = servers
        # The total number of entries returned.
        self.total_count = total_count

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Servers'] = []
        if self.servers is not None:
            for k1 in self.servers:
                result['Servers'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.servers = []
        if m.get('Servers') is not None:
            for k1 in m.get('Servers'):
                temp_model = main_models.ListServerGroupServersResponseBodyServers()
                self.servers.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServerGroupServersResponseBodyServers(DaraModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        remote_ip_enabled: bool = None,
        server_group_id: str = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        status: str = None,
        weight: int = None,
    ):
        # The description of the backend server.
        self.description = description
        # The port used by the backend server. Valid values: **1** to **65535**.
        self.port = port
        # Indicates whether the remote IP address feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.remote_ip_enabled = remote_ip_enabled
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The ID of the backend server.
        # 
        # > If **ServerType** is set to **Fc**, **ServerId** is the ARN of a function.
        self.server_id = server_id
        # The IP address in inclusive ENI mode.
        self.server_ip = server_ip
        # The type of the backend server.
        self.server_type = server_type
        # The status of the backend server. Valid values:
        # 
        # *   **Adding**
        # *   **Available**
        # *   **Configuring**
        # *   **Removing**
        self.status = status
        # The weight of the backend server. An ECS instance with a higher weight receives more requests.
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

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

