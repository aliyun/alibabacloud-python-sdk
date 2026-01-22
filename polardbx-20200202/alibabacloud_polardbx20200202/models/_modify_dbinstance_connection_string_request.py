# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringRequest(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_name: str = None,
        new_port: str = None,
        new_prefix: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.connection_string = connection_string
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.new_port = new_port
        # This parameter is required.
        self.new_prefix = new_prefix
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.new_port is not None:
            result['NewPort'] = self.new_port

        if self.new_prefix is not None:
            result['NewPrefix'] = self.new_prefix

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('NewPort') is not None:
            self.new_port = m.get('NewPort')

        if m.get('NewPrefix') is not None:
            self.new_prefix = m.get('NewPrefix')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

