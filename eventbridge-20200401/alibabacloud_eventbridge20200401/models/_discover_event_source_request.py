# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class DiscoverEventSourceRequest(DaraModel):
    def __init__(
        self,
        source_my_sqlparameters: main_models.DiscoverEventSourceRequestSourceMySQLParameters = None,
    ):
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
            temp_model = main_models.DiscoverEventSourceRequestSourceMySQLParameters()
            self.source_my_sqlparameters = temp_model.from_map(m.get('SourceMySQLParameters'))

        return self

class DiscoverEventSourceRequestSourceMySQLParameters(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        host_name: str = None,
        limit: str = None,
        network_type: str = None,
        offset: str = None,
        password: str = None,
        port: int = None,
        region_id: str = None,
        security_group_id: str = None,
        table_name: str = None,
        user: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.database_name = database_name
        self.host_name = host_name
        self.limit = limit
        self.network_type = network_type
        self.offset = offset
        self.password = password
        self.port = port
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.table_name = table_name
        self.user = user
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.user is not None:
            result['User'] = self.user

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

