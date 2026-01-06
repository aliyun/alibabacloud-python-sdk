# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourcePostgreSQLParameters(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        host_name: str = None,
        network_type: str = None,
        password: str = None,
        port: int = None,
        region_id: str = None,
        schema_name: str = None,
        security_group_id: str = None,
        snapshot_mode: str = None,
        table_names: str = None,
        user: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.database_name = database_name
        self.host_name = host_name
        self.network_type = network_type
        self.password = password
        self.port = port
        self.region_id = region_id
        self.schema_name = schema_name
        self.security_group_id = security_group_id
        self.snapshot_mode = snapshot_mode
        self.table_names = table_names
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

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.snapshot_mode is not None:
            result['SnapshotMode'] = self.snapshot_mode

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

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SnapshotMode') is not None:
            self.snapshot_mode = m.get('SnapshotMode')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

