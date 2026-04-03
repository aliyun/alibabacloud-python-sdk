# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFunagentInput(DaraModel):
    def __init__(
        self,
        admin_name: str = None,
        admin_secret: str = None,
        cpu: float = None,
        db_connections: int = None,
        db_host: str = None,
        db_instance_id: str = None,
        db_name: str = None,
        db_password: str = None,
        db_port: int = None,
        db_type: str = None,
        db_username: str = None,
        description: str = None,
        fun_agent_name: str = None,
        memory: int = None,
        region_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitch_ids: str = None,
    ):
        # `string`，必填
        # 
        # This parameter is required.
        self.admin_name = admin_name
        # `string`，必填
        # 
        # This parameter is required.
        self.admin_secret = admin_secret
        # `float64`，必填
        # 
        # This parameter is required.
        self.cpu = cpu
        # `int32`，必填
        # 
        # This parameter is required.
        self.db_connections = db_connections
        # `string`，必填
        # 
        # This parameter is required.
        self.db_host = db_host
        # `string`，必填
        self.db_instance_id = db_instance_id
        # `string`，必填
        # 
        # This parameter is required.
        self.db_name = db_name
        # `string`，必填
        # 
        # This parameter is required.
        self.db_password = db_password
        # `int32`，必填
        # 
        # This parameter is required.
        self.db_port = db_port
        # `string`，必填
        # 
        # This parameter is required.
        self.db_type = db_type
        # `string`，必填
        # 
        # This parameter is required.
        self.db_username = db_username
        # `string`，必填
        # 
        # This parameter is required.
        self.description = description
        # `string`，必填
        # 
        # This parameter is required.
        self.fun_agent_name = fun_agent_name
        # `int32`，必填
        # 
        # This parameter is required.
        self.memory = memory
        # 可选； `omitempty`
        self.region_id = region_id
        # `int32`，必填
        # 
        # This parameter is required.
        self.replicas = replicas
        # `string`，必填
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # `string`，必填
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # `string`，必填；JSON 数组 [{vswitchId, zoneId}]（core 解码为 `*string` 但校验非空）
        # 
        # This parameter is required.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_name is not None:
            result['adminName'] = self.admin_name

        if self.admin_secret is not None:
            result['adminSecret'] = self.admin_secret

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.db_connections is not None:
            result['dbConnections'] = self.db_connections

        if self.db_host is not None:
            result['dbHost'] = self.db_host

        if self.db_instance_id is not None:
            result['dbInstanceId'] = self.db_instance_id

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.db_password is not None:
            result['dbPassword'] = self.db_password

        if self.db_port is not None:
            result['dbPort'] = self.db_port

        if self.db_type is not None:
            result['dbType'] = self.db_type

        if self.db_username is not None:
            result['dbUsername'] = self.db_username

        if self.description is not None:
            result['description'] = self.description

        if self.fun_agent_name is not None:
            result['funAgentName'] = self.fun_agent_name

        if self.memory is not None:
            result['memory'] = self.memory

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.replicas is not None:
            result['replicas'] = self.replicas

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adminName') is not None:
            self.admin_name = m.get('adminName')

        if m.get('adminSecret') is not None:
            self.admin_secret = m.get('adminSecret')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('dbConnections') is not None:
            self.db_connections = m.get('dbConnections')

        if m.get('dbHost') is not None:
            self.db_host = m.get('dbHost')

        if m.get('dbInstanceId') is not None:
            self.db_instance_id = m.get('dbInstanceId')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dbPassword') is not None:
            self.db_password = m.get('dbPassword')

        if m.get('dbPort') is not None:
            self.db_port = m.get('dbPort')

        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')

        if m.get('dbUsername') is not None:
            self.db_username = m.get('dbUsername')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('funAgentName') is not None:
            self.fun_agent_name = m.get('funAgentName')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')

        return self

