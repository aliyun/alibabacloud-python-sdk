# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class TestEventSourceConfigRequest(DaraModel):
    def __init__(
        self,
        source_my_sqlparameters: main_models.TestEventSourceConfigRequestSourceMySQLParameters = None,
    ):
        # The parameters that are configured if you specify MySQL as the event source.
        self.source_my_sqlparameters = source_my_sqlparameters

    def validate(self):
        if self.source_my_sqlparameters:
            self.source_my_sqlparameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_my_sqlparameters is not None:
            result['SourceMySQLParameters'] = self.source_my_sqlparameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceMySQLParameters') is not None:
            temp_model = main_models.TestEventSourceConfigRequestSourceMySQLParameters()
            self.source_my_sqlparameters = temp_model.from_map(m.get('SourceMySQLParameters'))

        return self

class TestEventSourceConfigRequestSourceMySQLParameters(DaraModel):
    def __init__(
        self,
        allowed_cidrs: str = None,
        database_name: str = None,
        host_name: str = None,
        network_type: str = None,
        password: str = None,
        port: int = None,
        region_id: str = None,
        security_group_id: str = None,
        table_names: str = None,
        user: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.allowed_cidrs = allowed_cidrs
        # The database name.
        self.database_name = database_name
        # The endpoint of the database.
        self.host_name = host_name
        # The network type.
        # 
        # Valid values:
        # 
        # *   PrivateNetwork
        # *   PublicNetwork
        self.network_type = network_type
        # The password that is used for authentication.
        self.password = password
        # The port that is used to connect to the database.
        self.port = port
        # The region ID.
        self.region_id = region_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The table name. The name must be prefixed with the database name. ${DatabaseName}.${TableName}
        self.table_names = table_names
        # The username that is used to log on to the database.
        self.user = user
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_cidrs is not None:
            result['AllowedCIDRs'] = self.allowed_cidrs

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        if self.user is not None:
            result['User'] = self.user

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedCIDRs') is not None:
            self.allowed_cidrs = m.get('AllowedCIDRs')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

