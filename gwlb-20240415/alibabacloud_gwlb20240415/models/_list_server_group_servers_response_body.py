# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
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
        # The number of entries per page.
        # 
        # Valid values: 1 to 1000.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The backend servers.
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
        port: int = None,
        server_group_id: str = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        status: str = None,
    ):
        # The backend server port. Valid values:
        # 
        # *   **6081**
        self.port = port
        # The server group ID.
        self.server_group_id = server_group_id
        # The backend server ID.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: Elastic Compute Service (ECS) instance
        # *   **Eni**: elastic network interface (ENI)
        # *   **Eci**: elastic container instance
        # *   **Ip**: IP address
        self.server_type = server_type
        # Indicates the status of the backend server. Valid values:
        # 
        # *   **Adding**: The backend server is being added.
        # *   **Available**: The backend server is available.
        # *   **Draining**: The backend server is in connection draining.
        # *   **Removing**: The backend server is being removed.
        # *   **Replacing**: The backend server is being replaced.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

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

        return self

