# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddHDMInstanceRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        flush_account: str = None,
        instance_alias: str = None,
        instance_area: str = None,
        instance_id: str = None,
        ip: str = None,
        network_type: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        username: str = None,
        vpc_id: str = None,
        context: str = None,
    ):
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **SQLServer**
        # *   **PolarDBMySQL**
        # *   **PolarDBPostgreSQL**
        # *   **Redis**
        # *   **MongoDB**
        # *   **PolarDBOracle**
        # *   **PolarDBX**
        self.engine = engine
        # The reserved parameter.
        self.flush_account = flush_account
        # The name of the instance.
        self.instance_alias = instance_alias
        # The type of the instance on which the database is deployed. Valid values:
        # 
        # *   **RDS**: an Alibaba Cloud database instance.
        # *   **ECS**: an Elastic Compute Service (ECS) instance on which a self-managed database is deployed.
        # *   **IDC**: a self-managed database instance that is not deployed on Alibaba Cloud.
        # 
        # >  IDC refers to your data center.
        # 
        # This parameter is required.
        self.instance_area = instance_area
        # The instance ID.
        self.instance_id = instance_id
        # The endpoint that is used to access the instance over internal networks.
        self.ip = ip
        # The network type of the instance.
        self.network_type = network_type
        # The password for the username.
        self.password = password
        # The port that is used to access the instance over internal networks.
        self.port = port
        # The ID of the region in which the instance resides.
        self.region = region
        # The username that is used to log on to the database.
        self.username = username
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The reserved parameter.
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.flush_account is not None:
            result['FlushAccount'] = self.flush_account

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.username is not None:
            result['Username'] = self.username

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.context is not None:
            result['__context'] = self.context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('FlushAccount') is not None:
            self.flush_account = m.get('FlushAccount')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('__context') is not None:
            self.context = m.get('__context')

        return self

