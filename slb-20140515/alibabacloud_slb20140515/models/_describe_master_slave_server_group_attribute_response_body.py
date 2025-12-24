# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeMasterSlaveServerGroupAttributeResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        load_balancer_id: str = None,
        master_slave_backend_servers: main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServers = None,
        master_slave_server_group_id: str = None,
        master_slave_server_group_name: str = None,
        request_id: str = None,
        tags: main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyTags = None,
    ):
        # The time when the CLB instance was created. The time follows the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The ID of the associated CLB instance.
        self.load_balancer_id = load_balancer_id
        # A list of backend servers in the primary/secondary server group.
        self.master_slave_backend_servers = master_slave_backend_servers
        # The ID of the primary/secondary server group.
        self.master_slave_server_group_id = master_slave_server_group_id
        # The name of the primary/secondary server group.
        self.master_slave_server_group_name = master_slave_server_group_name
        # The request ID.
        self.request_id = request_id
        # The tag list.
        self.tags = tags

    def validate(self):
        if self.master_slave_backend_servers:
            self.master_slave_backend_servers.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.master_slave_backend_servers is not None:
            result['MasterSlaveBackendServers'] = self.master_slave_backend_servers.to_map()

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.master_slave_server_group_name is not None:
            result['MasterSlaveServerGroupName'] = self.master_slave_server_group_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MasterSlaveBackendServers') is not None:
            temp_model = main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServers()
            self.master_slave_backend_servers = temp_model.from_map(m.get('MasterSlaveBackendServers'))

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('MasterSlaveServerGroupName') is not None:
            self.master_slave_server_group_name = m.get('MasterSlaveServerGroupName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeMasterSlaveServerGroupAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMasterSlaveServerGroupAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key. Valid values of N: **1** to **20**. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.tag_key = tag_key
        # The tag value. Valid values of N: **1** to **20**. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServers(DaraModel):
    def __init__(
        self,
        master_slave_backend_server: List[main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer] = None,
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
                temp_model = main_models.DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer()
                self.master_slave_backend_server.append(temp_model.from_map(k1))

        return self

class DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer(DaraModel):
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
        # The ID of the backend server.
        self.server_id = server_id
        # The type of backend server. Valid values: **Master** and **Slave**.
        self.server_type = server_type
        # The type of the backend server. Valid values:
        # 
        # *   **ecs** (default): Elastic Compute Service (ECS) instance
        # *   **eni**: elastic network interface (ENI)
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

