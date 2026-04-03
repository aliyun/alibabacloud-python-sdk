# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Funagent(DaraModel):
    def __init__(
        self,
        admin_name: str = None,
        admin_secret: str = None,
        cpu: float = None,
        created_at: str = None,
        db_connections: int = None,
        db_host: str = None,
        db_instance_id: str = None,
        db_name: str = None,
        db_password: str = None,
        db_port: int = None,
        db_type: str = None,
        db_username: str = None,
        description: str = None,
        endpoint: str = None,
        funagent_id: str = None,
        funagent_name: str = None,
        image_url: str = None,
        memory: int = None,
        region_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        status: str = None,
        tenant_id: str = None,
        updated_at: str = None,
        version: str = None,
        vpc_id: str = None,
        vswitch_ids: str = None,
    ):
        self.admin_name = admin_name
        # 敏感；响应中应脱敏
        self.admin_secret = admin_secret
        self.cpu = cpu
        # ISO 8601
        self.created_at = created_at
        self.db_connections = db_connections
        self.db_host = db_host
        self.db_instance_id = db_instance_id
        self.db_name = db_name
        # 敏感；响应中应脱敏
        self.db_password = db_password
        self.db_port = db_port
        self.db_type = db_type
        self.db_username = db_username
        self.description = description
        self.endpoint = endpoint
        # UUID 字符串
        self.funagent_id = funagent_id
        self.funagent_name = funagent_name
        self.image_url = image_url
        self.memory = memory
        self.region_id = region_id
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.status = status
        self.tenant_id = tenant_id
        # ISO 8601
        self.updated_at = updated_at
        self.version = version
        self.vpc_id = vpc_id
        # 与存储一致时为 JSON 字符串
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

        if self.created_at is not None:
            result['createdAt'] = self.created_at

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

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.funagent_id is not None:
            result['funagentId'] = self.funagent_id

        if self.funagent_name is not None:
            result['funagentName'] = self.funagent_name

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.memory is not None:
            result['memory'] = self.memory

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.replicas is not None:
            result['replicas'] = self.replicas

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.version is not None:
            result['version'] = self.version

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

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

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

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('funagentId') is not None:
            self.funagent_id = m.get('funagentId')

        if m.get('funagentName') is not None:
            self.funagent_name = m.get('funagentName')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')

        return self

