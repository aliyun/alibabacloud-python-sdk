# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEngineMigrationRequest(DaraModel):
    def __init__(
        self,
        connection_strings: str = None,
        dbinstance_name: str = None,
        new_master_dbinstance_name: str = None,
        region_id: str = None,
        source_dbinstance_name: str = None,
        swap_connection_string: str = None,
    ):
        # The specific endpoints to switch. Set this parameter to a JSON string that contains the pairs of endpoints to swap.
        # > This parameter takes effect only when SwapConnectionString is set to true.
        self.connection_strings = connection_strings
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The name of the new primary instance after the migration is complete.
        self.new_master_dbinstance_name = new_master_dbinstance_name
        # The region ID.
        self.region_id = region_id
        # The name of the source database instance.
        self.source_dbinstance_name = source_dbinstance_name
        # Specifies whether to automatically swap connection strings. Valid values:
        # 
        # - true: The application does not need to modify its configuration. Connections are automatically directed to the new instance.
        # 
        # - false: You must manually update the application endpoint.
        self.swap_connection_string = swap_connection_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_strings is not None:
            result['ConnectionStrings'] = self.connection_strings

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.new_master_dbinstance_name is not None:
            result['NewMasterDBInstanceName'] = self.new_master_dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_dbinstance_name is not None:
            result['SourceDBInstanceName'] = self.source_dbinstance_name

        if self.swap_connection_string is not None:
            result['SwapConnectionString'] = self.swap_connection_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStrings') is not None:
            self.connection_strings = m.get('ConnectionStrings')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('NewMasterDBInstanceName') is not None:
            self.new_master_dbinstance_name = m.get('NewMasterDBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceDBInstanceName') is not None:
            self.source_dbinstance_name = m.get('SourceDBInstanceName')

        if m.get('SwapConnectionString') is not None:
            self.swap_connection_string = m.get('SwapConnectionString')

        return self

