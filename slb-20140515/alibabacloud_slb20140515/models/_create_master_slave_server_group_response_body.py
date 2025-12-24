# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateMasterSlaveServerGroupResponseBody(DaraModel):
    def __init__(
        self,
        master_slave_backend_servers: main_models.CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServers = None,
        master_slave_server_group_id: str = None,
        request_id: str = None,
    ):
        # The backend servers in the primary/secondary server group.
        self.master_slave_backend_servers = master_slave_backend_servers
        # The ID of the active/standby server group.
        self.master_slave_server_group_id = master_slave_server_group_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.master_slave_backend_servers:
            self.master_slave_backend_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_slave_backend_servers is not None:
            result['MasterSlaveBackendServers'] = self.master_slave_backend_servers.to_map()

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterSlaveBackendServers') is not None:
            temp_model = main_models.CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServers()
            self.master_slave_backend_servers = temp_model.from_map(m.get('MasterSlaveBackendServers'))

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServers(DaraModel):
    def __init__(
        self,
        master_slave_backend_server: List[main_models.CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer] = None,
    ):
        self.master_slave_backend_server = master_slave_backend_server

    def validate(self):
        if self.master_slave_backend_server:
            for v1 in self.master_slave_backend_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MasterSlaveBackendServer'] = []
        if self.master_slave_backend_server is not None:
            for k1 in self.master_slave_backend_server:
                result['MasterSlaveBackendServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_slave_backend_server = []
        if m.get('MasterSlaveBackendServer') is not None:
            for k1 in m.get('MasterSlaveBackendServer'):
                temp_model = main_models.CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer()
                self.master_slave_backend_server.append(temp_model.from_map(k1))

        return self

class CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer(DaraModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_type: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The description of the primary/secondary server group.
        self.description = description
        # The port that is used by the backend server.
        self.port = port
        # The ID of the backend server that you want to add.
        self.server_id = server_id
        # The type of backend server.
        # 
        # Valid values: **Master** and **Slave**.
        self.server_type = server_type
        # The type of backend server. Valid values:
        # 
        # *   **ecs**: ECS instance
        # *   **eni**: ENI
        # *   **eci**: elastic container instance
        self.type = type
        # The weight of the backend server.
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

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

